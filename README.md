# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.13 — Recovery Resume

[Download v0.18.13](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.13).

Existing installations: open **Settings → CHECK UPDATE**, wait for workers to stop, then close the Controller. The signed updater preserves runtime state, checkpoints, statistics, sessions and reward history. An active checkpoint defers installation; do not Reset a batch merely to install this update.

This release keeps Resume available after Stop during blocked Universal recovery, and preserves Heart exclusion and archive-before-new-Start authority. Reward Archive and Send Log code remains unchanged from v0.18.12.

Validation: 1,053 tests passed, 17 skipped; signed upgrades from v0.18.11 and v0.18.12 preserved nine runtime files each byte-for-byte. Native Windows/LDPlayer validation remains pending.

ZIP SHA-256: `5fedaf38b5e8608c9f60e62c758b9ea27082e8ec8101728a99e29418b956211f`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater checks the feed in the background and installs only when both Universal and Heart have no active worker or checkpoint. A running continuous batch is never paused or reset for an update. A failed package swap restores backed-up code files. Runtime state is retained.

Published v0.18.0 ZIP SHA-256: `4cef7cc02bb2247120c08ea04c342f7a9e3459e7bfceb19394899a731ba9f141`.

The signing private key is not stored in this repository or any release asset. `updates.json` is signed; release archive and every included file must match its signed hashes.
