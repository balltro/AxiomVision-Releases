#!/usr/bin/env python3
"""Reproduce the signed release from verified v0.18.12 bytes; no private key."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import zipfile
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

ROOT = Path(__file__).resolve().parent
PUBLIC_KEY = "19/Zi/3tnbD2eizw8Jjl4D1FPDbZsfGlMWKAJv5a420="
VERSION_FILES = (
    "RUN-SETUP-WINDOWS.bat",
    "visionstudio/.codex-plugin/plugin.json",
    "visionstudio/scripts/visionstudio_controller.py",
    "visionstudio/scripts/visionstudio_bridge.py",
    "visionstudio/scripts/visionstudio_local_runner.py",
    "visionstudio/scripts/visionstudio_heart_contract.py",
    "visionstudio/scripts/verify_runtime_version.py",
    "visionstudio/scripts/setup-windows.ps1",
    "visionstudio/tests/test_runtime_version.py",
    "visionstudio/tests/test_bridge.py",
    "visionstudio/tests/test_controller_state.py",
    "visionstudio/tests/test_local_runner.py",
    "visionstudio/tests/test_heart_runner.py",
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def verified_envelope(path: Path) -> dict:
    envelope = json.loads(path.read_bytes())
    Ed25519PublicKey.from_public_bytes(base64.b64decode(PUBLIC_KEY)).verify(
        base64.b64decode(envelope["signature"]), canonical(envelope["release"])
    )
    return envelope["release"]


def main() -> None:
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--base-directory", type=Path)
    source.add_argument("--base-zip", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--signed-feed", type=Path)
    args = parser.parse_args()
    baseline = verified_envelope(ROOT / "baseline-feed.json")
    assert baseline["version"] == "0.18.12"
    names = baseline["files"]
    if args.base_zip:
        assert sha(args.base_zip.read_bytes()) == baseline["sha256"], "Baseline archive hash mismatch"
        with zipfile.ZipFile(args.base_zip) as archive:
            entries = [entry.filename for entry in archive.infolist() if not entry.is_dir()]
            assert len(entries) == len(names) and set(entries) == set(names)
            files = {name: archive.read(name) for name in names}
    else:
        files = {name: (args.base_directory / name).read_bytes() for name in names}
    assert all(sha(value) == names[name] for name, value in files.items()), "Baseline member hash mismatch"
    controller = "visionstudio/scripts/visionstudio_controller.py"
    before = (ROOT / "controller-boundary-before.txt").read_bytes()
    after = (ROOT / "controller-boundary-after.txt").read_bytes()
    assert files[controller].count(before) == 1, "Controller patch precondition failed"
    files[controller] = files[controller].replace(before, after, 1)
    for name in VERSION_FILES:
        files[name] = files[name].replace(b"0.18.12", b"0.18.13").replace(
            b"codex.20261006.recovery", b"codex.20261008.recovery-resume"
        ).replace(b"0.18.13-recovery-300", b"0.18.13-recovery-resume-300")
    plugin = "visionstudio/.codex-plugin/plugin.json"
    manifest = json.loads(files[plugin])
    manifest["interface"]["longDescription"] = (
        "Axiom Vision v0.18.13 retains Resume, mutual exclusion, and archive-before-Start authority "
        "for stopped blocked Universal checkpoints. Existing recovery, native input guards, Reward "
        "Archive, single-file Send Log, Universal Revision 9 and Heart Revision 13 are preserved."
    )
    files[plugin] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    for package_name, prefix in (
        ("visionstudio/README_TH.md", "readme-prefix.txt"),
        ("visionstudio/AGENTS.md", "agents-prefix.txt"),
    ):
        files[package_name] = (ROOT / prefix).read_bytes() + files[package_name]
    files["visionstudio/RELEASE_v0.18.13_TH.md"] = (ROOT / "release-notes.md").read_bytes()
    files["visionstudio/tests/test_recovery_controller_boundary.py"] = (
        ROOT / "test_recovery_controller_boundary.py"
    ).read_bytes()
    files["visionstudio/update-package-files.json"] = (
        json.dumps(sorted(files), ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    assert len(files) == 121
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Stored entries with fixed metadata reproduce exactly across Python/zlib versions.
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, value in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 8, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, value)
    if args.signed_feed:
        release = verified_envelope(args.signed_feed)
        assert release["version"] == "0.18.13"
        assert release["sha256"] == sha(args.output.read_bytes()), "Candidate archive hash mismatch"
        assert release["files"] == {name: sha(value) for name, value in files.items()}
        assert release["requirements_sha256"] == sha(files["visionstudio/requirements-windows.txt"])
    print(json.dumps({"version": "0.18.13", "files": len(files),
                      "size": args.output.stat().st_size, "sha256": sha(args.output.read_bytes())}))


if __name__ == "__main__":
    main()
