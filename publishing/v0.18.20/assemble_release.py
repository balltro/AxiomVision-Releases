#!/usr/bin/env python3
"""Reproduce v0.18.20 from signed v0.18.19 and exact reviewed text patches."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import zipfile
from pathlib import Path, PurePosixPath

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

ROOT = Path(__file__).resolve().parent
PUBLIC_KEY = "19/Zi/3tnbD2eizw8Jjl4D1FPDbZsfGlMWKAJv5a420="


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def verified_release(path: Path) -> dict:
    envelope = json.loads(path.read_bytes())
    Ed25519PublicKey.from_public_bytes(base64.b64decode(PUBLIC_KEY)).verify(
        base64.b64decode(envelope["signature"]), canonical(envelope["release"])
    )
    return envelope["release"]


def safe_path(name: str) -> str:
    assert isinstance(name, str) and "\\" not in name and ":" not in name
    path = PurePosixPath(name)
    assert not path.is_absolute() and not any(p in {".", "..", ""} for p in name.split("/"))
    assert name == "RUN-SETUP-WINDOWS.bat" or name.startswith("visionstudio/")
    assert not name.startswith(tuple("visionstudio/" + part + "/" for part in ("controller", "checkpoints", "sessions", "stats")))
    return name


def main() -> None:
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--base-directory", type=Path)
    source.add_argument("--base-zip", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--signed-feed", type=Path)
    args = parser.parse_args()
    baseline = verified_release(ROOT / "baseline-feed.json")
    assert baseline["version"] == "0.18.19"
    if args.base_zip:
        assert sha(args.base_zip.read_bytes()) == baseline["sha256"]
        with zipfile.ZipFile(args.base_zip) as archive:
            names = [m.filename for m in archive.infolist() if not m.is_dir()]
            assert len(names) == len(baseline["files"]) and set(names) == set(baseline["files"])
            files = {safe_path(name): archive.read(name) for name in names}
    else:
        files = {safe_path(name): (args.base_directory / name).read_bytes() for name in baseline["files"]}
    assert {name: sha(value) for name, value in files.items()} == baseline["files"]
    changes = json.loads((ROOT / "source-changes.json").read_bytes())
    for change in changes:
        name = safe_path(change["path"])
        if change["before_sha256"] is None:
            assert name not in files
            value = change["content"].encode("utf-8")
        else:
            assert sha(files[name]) == change["before_sha256"], name
            lines = files[name].decode("utf-8").splitlines(keepends=True)
            for edit in reversed(change["edits"]):
                start, end = edit["start"], edit["end"]
                assert "".join(lines[start:end]) == edit["before"], name
                lines[start:end] = edit["after"].splitlines(keepends=True)
            value = "".join(lines).encode("utf-8")
        assert sha(value) == change["after_sha256"], name
        files[name] = value
    assert set(json.loads(files["visionstudio/update-package-files.json"])) == set(files)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, value in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 23, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, value)
    if args.signed_feed:
        release = verified_release(args.signed_feed)
        assert release["version"] == "0.18.20"
        assert release["sha256"] == sha(args.output.read_bytes())
        assert release["files"] == {name: sha(value) for name, value in files.items()}
        assert release["requirements_sha256"] == sha(files["visionstudio/requirements-windows.txt"])
    print(json.dumps({"version": "0.18.20", "files": len(files), "size": args.output.stat().st_size,
                      "sha256": sha(args.output.read_bytes())}))


if __name__ == "__main__":
    main()
