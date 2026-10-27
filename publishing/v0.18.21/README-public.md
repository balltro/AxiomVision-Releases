# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.21 — Relay Logs on Windows

[Download v0.18.21](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.21).

Fixes the Windows Relay diagnostic reader introduced in v20. Windows DirEntry.stat caches zero file identity fields; comparing those cached values with the real open file handle rejected every selected journal. The reader now compares fresh non-following path metadata with the opened regular file's identity, preserves replacement/symlink checks, and binds its bounded tail read to the handle's captured size. Read failures carry fixed safe reason codes.

The publisher is gated by native Windows Python3.12.10 validation: the v20 reader must fail on an unchanged readable journal while v21 reads the retained event. The complete Relay diagnostics suite, including production bundle creation and exact Telegram excerpt retention, must also pass there before publication. This validates diagnostic file reads, not LDPlayer screen capture, click timing or game acceptance.

The Oct28 diagnostic selected64 of8,922 retained journals but read0bytes because all64 reads failed. Its installed package is v20 while the five attached runtime journals remain historical v19 records. Zero returned events in this report do not prove that Relay did not run, and historical recovery failures do not establish a v20 regression.

Validation: **1,275 passed / 17 skipped (1,292 total)** on the host, including19 reader tests. Independent source/privacy/bounds review passed. Signed upgrades from v0.18.13–v0.18.20 verify all161 package members and preserve nine runtime files per installation, including readable timing presets. Relay/Recovery/native input behavior and frozen Plans remain unchanged (OFF revision9, ON revision11).

Use **Settings → CHECK UPDATE** while workers are stopped and installation is eligible, reopen the Controller, then **SEND LOG** to collect retained history from existing files. Collecting diagnostics requires no new farming batch. Presets and runtime data are retained; AUTO still disables Relay.

ZIP SHA-256: `e3eb419d924a7ad5398788ca1404e379e5bf241586e5278e7253c156fb34539d`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater installs only when both Universal and Heart are idle and no active checkpoint remains. A failed package swap restores backed-up code files. The signing private key is not stored in this repository or a release asset; the archive and every included file must match the signed hashes in `updates.json`.
