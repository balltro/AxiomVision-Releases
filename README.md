# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.15 — Recovery Watchdog

[Download v0.18.15](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.15).

Existing installations: open **Settings → CHECK UPDATE**, stop workers, then close the Controller. The signed updater preserves runtime state, checkpoints, statistics, sessions and historical reward files. An active checkpoint defers installation; do not Reset a batch merely to install this update.

A verified frozen Universal worker can now enter guarded checkpoint recovery before `resume_required` was set. Input locks before confirmed process-tree termination, and the durable recovery queue preserves Stop/Pause/Human, Plan, geometry, pending intent and never-replay protections. A fresh-frame warning no longer hides an unresponsive worker. Unscheduled or terminal blocks display their actual status.

Send Log retains compact failure/recovery history separately from normal tails and prioritizes the current mission's preview. Coverage is bounded and explicit; previews never grant input authority. Runtime item/treasure image reading and catalog UI remain disabled.

Validation: 1,118 tests passed, 17 skipped (1,135 total). Signed upgrades from v0.18.12, v0.18.13 and v0.18.14 preserve nine runtime files byte-for-byte per installation. Universal Revision 9, Heart Revision 13 and dependency pins remain unchanged. Windows process termination is covered by simulation; native Windows/LDPlayer validation remains pending.

ZIP SHA-256: `2c5429aa1ed68ab55f5b03f4d36b50fab0ba73689d0c6e8e7f453cd318b2a198`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater checks the feed in the background and installs only when both Universal and Heart have no active worker or checkpoint. A running continuous batch is never paused or reset for an update. A failed package swap restores backed-up code files. Runtime state is retained.

Published v0.18.0 ZIP SHA-256: `4cef7cc02bb2247120c08ea04c342f7a9e3459e7bfceb19394899a731ba9f141`.

The signing private key is not stored in this repository or any release asset. `updates.json` is signed; release archive and every included file must match its signed hashes.
