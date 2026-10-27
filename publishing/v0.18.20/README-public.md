# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.20 — Recovery Observation

[Download v0.18.20](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.20).

Fixes Stage recovery after an expired Multi-Buy input lockout. Recovery previously rejected the fresh observation required to clear that lockout, causing repeated blocked recovery attempts. The new exception permits only a read-only post-expiry capture, with final Session, Controller batch/Plan, Stage, intent, ledger, Human and window checks before acknowledging the same lockout. Pending and committed purchases retain their replay restrictions; Stage resume still needs scene confirmation.

SEND LOG now retains bounded, whitelisted Relay event history independently of the latest five session journals. A sequence of setup/recovery sessions can no longer displace all older retained Relay diagnostics. Coverage and omissions are explicit; summaries are telemetry only and are preserved exactly in the Telegram excerpt.

The supplied Oct27 diagnostic has Relay ON, Custom60s and revision11, but its five journals contain setup/recovery only. It cannot determine Relay detection or native input performance. This release fixes the demonstrated recovery deadlock and diagnostic retention. The direct RGB Relay matcher, native mouse path, thresholds and Plan remain unchanged. Native Windows/LDPlayer capture/input and game acceptance remain unverified.

Validation: **1,268 passed / 17 skipped (1,285 total)**. Existing v19 deadlock reproduces; corrected recovery preserves purchase state and blocks Stop/Pause/Human and same-Plan replacement batches. All91 tested config/Plan identities match v19 (OFF revision9, ON revision11). Signed upgrades from v0.18.13–v0.18.19 verify all160 package hashes and preserve nine runtime files per installation, including readable timing presets.

Use **Settings → CHECK UPDATE** with workers stopped and no active checkpoint, then reopen the Controller. Select the intended Run Profile and **COOKIE RELAY → ON** before a new batch. Presets save time only; AUTO disables Relay. Existing old revision10 Relay guidance still applies. Archives, statistics, sessions and timing presets are retained.

ZIP SHA-256: `6b09fb34d5cbae7a616197cd454e908e0899a809a9c74cfca27f3f9f8fcf106a`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater installs only when both Universal and Heart are idle and no active checkpoint remains. A failed package swap restores backed-up code files. The signing private key is not stored in this repository or a release asset; the archive and every included file must match the signed hashes in `updates.json`.
