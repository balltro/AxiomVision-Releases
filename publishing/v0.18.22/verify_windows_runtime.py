"""Native Windows gate for Mystery Box identification and durable reporting."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile
import zipfile


def load_reader(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


parser = argparse.ArgumentParser()
parser.add_argument("--base-zip", type=Path, required=True)
parser.add_argument("--candidate-zip", type=Path, required=True)
args = parser.parse_args()
assert sys.platform == "win32", "This gate requires native Windows"
assert sys.version_info[:3] == (3, 12, 10), "Match the user's Python 3.12.10"
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

with tempfile.TemporaryDirectory(prefix="axiom-box-native-") as temporary:
    root = Path(temporary)
    baseline, candidate = root / "baseline", root / "candidate"
    # assemble_release.py verified both signed archives and their safe paths
    # in the immediately preceding workflow step.
    for archive_path, destination in ((args.base_zip, baseline), (args.candidate_zip, candidate)):
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(destination)
    sessions = root / "sessions"
    sessions.mkdir()
    journal = sessions / "retained-running.jsonl"
    journal.write_text(json.dumps({
        "event": "cookie_relay_watch_summary", "session_id": "a" * 32,
        "stage_id": "passive-running", "ledger_status": "ready",
        "metrics": {"samples": 17, "visual_matches": 0, "no_visual_match": 17},
    }) + "\n", encoding="utf-8")
    with os.scandir(sessions) as entries:
        cached = next(entries).stat(follow_symlinks=False)
    fresh = os.stat(journal, follow_symlinks=False)
    with journal.open("rb") as source:
        opened = os.fstat(source.fileno())
    assert (cached.st_ino, cached.st_dev) == (0, 0)
    assert fresh.st_ino != 0
    assert (fresh.st_ino, fresh.st_dev) == (opened.st_ino, opened.st_dev)
    for version, package in (("v21", baseline), ("v22", candidate)):
        reader = load_reader("relay_reader_" + version,
            package / "visionstudio/scripts/visionstudio_relay_diagnostics.py")
        content, coverage = reader.relay_history_snapshot(sessions)
        assert coverage["events_returned"] == 1
        assert "read_error" not in coverage["sources_newest_first"][0]
        assert json.loads(content.splitlines()[0])["metrics"]["samples"] == 17
    test_root = candidate / "visionstudio"
    results = []
    for pattern in (
        "test_mystery_box_pixels.py", "test_mystery_box_pixel_pipeline.py",
        "test_mystery_box_evidence.py", "test_relay_diagnostics.py", "test_runtime_version.py",
    ):
        checked = subprocess.run([
            sys.executable, "-m", "unittest", "discover", "-s", str(test_root / "tests"),
            "-p", pattern, "-v",
        ], cwd=test_root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
        print(checked.stdout, end="")
        print(checked.stderr, end="")
        assert checked.returncode == 0, pattern + " failed on native Windows"
        match = re.search(r"Ran (\d+) tests? in ([0-9.]+)s", checked.stderr)
        assert match, "Native test result missing: " + pattern
        assert "skipped=" not in checked.stderr, "Required native tests must run: " + pattern
        results.append({"suite": pattern, "passed": int(match[1]), "seconds": float(match[2])})
    print(json.dumps({
        "type": "axiom.windows_mystery_box_validation", "version": "0.18.22",
        "platform": platform.platform(), "python": platform.python_version(),
        "native_windows_tested": True, "suites": results,
        "tests_passed": sum(row["passed"] for row in results),
        "native_path_and_handle_identity_match": True,
        "relay_history_reader_compatibility_preserved": True,
        "pixel_types_counts_and_stability_tested": True,
        "restore_loop_record_ui_telegram_pipeline_tested": True,
        "bounded_hash_bound_evidence_and_telegram_tested": True,
        "native_ldplayer_capture_or_input_tested": False,
        "original_preopen_sprite_artwork_tested": False,
    }, sort_keys=True))
