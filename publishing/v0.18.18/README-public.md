# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.18 — Relay Response

[Download v0.18.18](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.18).

Fixes a Cookie Relay input block for asymmetric LDPlayer chrome. Replaying the supplied Relay image in the diagnostic’s 1642×941 layout puts the valid card at x714 while the old allowed region starts at x722. Detection succeeds but the old guard rejects before intent. Five retained diagnostic Running intervals show Relay enabled and scheduled, with no prepared input. The missed live pixels were not retained, so this is a reproduced code/layout defect consistent with the log.

Relay ON now uses **revision 11 / visual-2**. Its corrected left envelope still requires the complete fresh prompt, all yellow/green edges and both Running controls. One-pixel border sampling is more robust. The private path checks Human Verification once per immutable frame, measures only the proven Relay ROI with the same freshness thresholds, and retains the **0.5-second capture-start witness limit** and durable never-replay ledger. One monitor-end summary reports negative scans and pre-intent rejection reasons without logging every fast sample.

**Existing unfinished Relay revision 10 batch:** Stop, then **Reset Batch** to archive it before starting the new plan. Start/Resume/automatic recovery cannot silently reinterpret or overwrite old authority. Saved timing presets remain. Relay OFF keeps exact revision 9 Plan identities.

Validation: **1,224 passed / 17 skipped (1,241 total)**. All 42 actual-image chrome phases and 15 visual negatives pass. Fourteen modeled two-second button windows pass with actual detectors, Controller/Plan checks, ROI freshness and durable I/O; capture/input adapters and phase clocks are simulated. Native Windows/LDPlayer timing and game acceptance remain unverified. Independent card-size animation is not calibrated.

Signed upgrades from v0.18.13–v0.18.17 preserve nine runtime files each byte-for-byte, including readable saved timing presets. All 152 package hashes match the frozen source. Heart Sender input, native mouse backend and dependency pins are unchanged. Stop/Pause/Human, foreground, geometry, watchdog and replay protections remain.

Existing installations: use **Settings → CHECK UPDATE**, stop workers, then close the Controller when installation is eligible. If an active checkpoint defers this Relay plan upgrade, Stop and Reset Batch first. Runtime archives, statistics, sessions and saved timing presets are retained.

ZIP SHA-256: `1aef624093ed45ed3fea0ccb21deeb7c919a5869147432c78e26ca88b2c93934`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater installs only when both Universal and Heart are idle and no active checkpoint remains. A failed package swap restores backed-up code files. The signing private key is not stored in this repository or a release asset; the archive and every included file must match the signed hashes in `updates.json`.
