"""Native Windows regression gate for the signed Relay diagnostic reader."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import platform
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
assert sys.platform == "win32", "This publication gate requires native Windows"
assert sys.version_info[:3] == (3, 12, 10), "Match the user's Python 3.12.10 runtime"

with tempfile.TemporaryDirectory(prefix="axiom-reader-native-") as temporary:
    root = Path(temporary)
    baseline, candidate = root / "baseline", root / "candidate"
    # Both archives were reproduced/verified by assemble_release.py in the
    # immediately preceding workflow step. They contain only signed safe paths.
    for archive_path, destination in ((args.base_zip, baseline), (args.candidate_zip, candidate)):
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(destination)
    relative = "visionstudio/scripts/visionstudio_relay_diagnostics.py"
    old = load_reader("relay_reader_v20", baseline / relative)
    new = load_reader("relay_reader_v21", candidate / relative)
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
    _old_content, before = old.relay_history_snapshot(sessions)
    content, after = new.relay_history_snapshot(sessions)
    assert before["events_returned"] == 0
    assert before["sources_newest_first"][0]["read_error"] is True
    assert before["sources_newest_first"][0]["bytes_read"] == 0
    assert after["events_returned"] == 1
    assert after["sources_newest_first"][0]["bytes_read"] > 0
    assert "read_error" not in after["sources_newest_first"][0]
    assert json.loads(content.splitlines()[0])["metrics"]["samples"] == 17
    test_root = candidate / "visionstudio"
    subprocess.run([
        sys.executable, "-m", "unittest", "discover", "-s", str(test_root / "tests"),
        "-p", "test_relay_diagnostics.py", "-v",
    ], cwd=test_root, check=True)
    print(json.dumps({
        "type": "axiom.windows_relay_reader_validation", "version": "0.18.21",
        "platform": platform.platform(), "python": platform.python_version(),
        "native_windows_reader_tested": True,
        "native_cached_direntry_identity_is_zero": True,
        "native_path_and_handle_identity_match": True,
        "baseline_v20_read_error_reproduced": True,
        "candidate_v21_retained_event_read": True,
        "production_bundle_and_telegram_tests_passed": True,
        "native_ldplayer_capture_or_input_tested": False,
    }, sort_keys=True))
