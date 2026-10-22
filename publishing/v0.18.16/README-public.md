# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.16 — Cookie Relay

[Download v0.18.16](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.16).

**COOKIE RELAY** now appears directly after Random Boost. It defaults to OFF. Select Short, Normal or Custom before enabling it; AUTO clears and disables Relay. With Relay ON, the profile duration means the approximate first-runner duration. The profile schedules rapid local visual checks; only a fresh recognized Relay prompt, card and Running controls permit the guarded input.

One stable preflight and a fresh dispatch witness protect the short button window. A separate durable never-replay intent/commit ledger prevents duplicate input across restart. Result retention, routing and loop statistics continue through the existing path. Native input commitment is logged separately from game acceptance.

Existing Relay-OFF plans retain exact revision9 hashes; Relay ON uses revision10 bound to its configuration, private guard and detector calibration. Stop/Pause/Human Verification, geometry, freshness, foreground and watchdog guards remain. Runtime item/treasure reading stays disabled.

Validation: 1,166 tests passed,17 skipped (1,183 total); source-image replay, timing/stop/restart simulations and actual Linux Tk UI captures passed. Signed upgrades from v0.18.13,v0.18.14,v0.18.15 preserve nine runtime files each byte-for-byte. Native Windows/LDPlayer timing and game acceptance remain unverified.

Existing installations: open **Settings → CHECK UPDATE**, stop workers, then close the Controller when installation is eligible. Active checkpoints defer installation; do not Reset a batch merely to install this update. Runtime state, statistics, sessions and historical rewards are retained.

ZIP SHA-256: `95451ad73e0d78f9a0c1ea83743c9ba4851c15b7237696df4528b4a2fab11242`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater checks the feed in the background and installs only when both Universal and Heart have no active worker or checkpoint. A running continuous batch is never paused or reset for an update. A failed package swap restores backed-up code files.

The signing private key is not stored in this repository or any release asset. `updates.json` is signed; release archive and every included file must match its signed hashes.
