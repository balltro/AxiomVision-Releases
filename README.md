# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## v0.18.0

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater checks the feed in the background and installs only when both Universal and Heart have no active worker or checkpoint. A running continuous batch is never paused or reset for an update. A failed package swap restores backed-up code files. Runtime state is retained.

Published v0.18.0 ZIP SHA-256: `4cef7cc02bb2247120c08ea04c342f7a9e3459e7bfceb19394899a731ba9f141`.

The signing private key is not stored in this repository or any release asset. `updates.json` is signed; release archive and every included file must match its signed hashes.
