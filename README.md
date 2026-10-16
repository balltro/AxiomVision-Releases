# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.14 — Recovery Core

[Download v0.18.14](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.14).

Existing installations: open **Settings → CHECK UPDATE**, wait for workers to stop, then close the Controller. The signed updater preserves runtime state, checkpoints, statistics, sessions and historical reward files. An active checkpoint defers installation; do not Reset a batch merely to install this update.

Runtime item/treasure image capture, background item OCR and the item catalog UI are removed. Run Summary retains authoritative Mystery Box counts, Coins and EXP; box collection and fresh scene/input guards remain active.

Recovery now supplements missed Confirm text from the same exact frame, allows one fresh observation before a first Confirm, and persists one guarded Local restore for a clean reward checkpoint before Codex. Validated note/reason metadata and private same-process abort proof preserve never-replay authority. Repeated observation does not inflate Recovered.

Validation: 1,088 tests passed, 17 skipped; signed upgrades from v0.18.11, v0.18.12 and v0.18.13 preserved nine runtime files each byte-for-byte. Send Log transport and the Universal Mission code are unchanged. Native Windows/LDPlayer validation remains pending.

ZIP SHA-256: `86f7f539c5702455c4cf13cf75ac816f4c3f0e708f5aba161d300a2a646ec9de`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater checks the feed in the background and installs only when both Universal and Heart have no active worker or checkpoint. A running continuous batch is never paused or reset for an update. A failed package swap restores backed-up code files. Runtime state is retained.

Published v0.18.0 ZIP SHA-256: `4cef7cc02bb2247120c08ea04c342f7a9e3459e7bfceb19394899a731ba9f141`.

The signing private key is not stored in this repository or any release asset. `updates.json` is signed; release archive and every included file must match its signed hashes.
