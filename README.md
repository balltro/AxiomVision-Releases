# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.19 — Relay Direct

[Download v0.18.19](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.19).

The guarded Cookie Relay path reads immutable native RGB buffers directly, reuses its thread-owned MSS capture context, and removes PNG encoding/decoding from the click decision. The same visual-2 Relay matcher, Human signature, target region, ROI thresholds, three witnesses, durable intent and 0.5-second capture-start limit remain. The mouse implementation and input/replay protections are unchanged.

Raw frame hashes use an explicit raw-rgb-v1 domain and are tagged separately from PNG evidence. The context closes on its owner monitor thread. A failed raw adapter blocks input; it never falls back to stale pixels. Existing pending/committed PNG Relay ledgers remain consumed after restore.

**Enable COOKIE RELAY → ON before starting the batch.** A timing preset saves seconds only. AUTO disables Relay. If the current frozen batch is OFF, Stop and Reset Batch before selecting a profile/preset, enabling ON and starting a new batch. The supplied v18 diagnostic is OFF, so it cannot establish enabled Relay latency. The UI now distinguishes the OFF and ON hints clearly.

Validation: **1,247 passed / 17 skipped (1,264 total)**. In real-clock replay with native grab/window/input adapters, the complete code transaction measured v18 median **584.725ms** versus v19 **183.405ms**, with 9/9 cases passing per version. Three additional two-second-window cases overlapping public sampling also pass. Classifiers, actual MSS conversion/PNG encoder, Controller/Plan checks, freshness and durable writes run. These are host code measurements, not native Windows/LDPlayer timing or game acceptance proof.

All 63 compiled config/Plan identities match v18: OFF revision9, ON revision11, visual-2 calibration unchanged. No new Plan migration is introduced. Older unfinished revision10 Relay batches still require the existing explicit Stop/Reset archive. Signed upgrades from v0.18.13–v0.18.18 preserve nine runtime files per installation byte-for-byte and retain saved timing presets. All 156 package hashes match frozen source.

Use **Settings → CHECK UPDATE**, stop workers, then close the Controller when installation is eligible. Active checkpoints defer installation. Reset only when changing a frozen OFF batch to ON or when the existing old-Plan guidance requires it. Archives, statistics, sessions and timing presets are retained.

ZIP SHA-256: `2dab8cec0991ad30bbdd0abfc0d8013d1419f54522e2ff6da0ea949dadc6279f`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater installs only when both Universal and Heart are idle and no active checkpoint remains. A failed package swap restores backed-up code files. The signing private key is not stored in this repository or a release asset; the archive and every included file must match the signed hashes in `updates.json`.
