# Axiom Vision Releases

Public Windows release assets and Ed25519-signed update feed for Axiom Vision.

## Latest: v0.18.17 — Run Profile Presets

[Download v0.18.17](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.17).

**TIME PRESET** sits below Run Profile. Use **SAVE AS** to name and save a duration (30–1,800 whole seconds), select it to apply Custom timing, or use **EDIT / DELETE**. Thai names and saved times persist immediately, across reopening and Reset Batch. Presets change timing only; Boost, Relay and loop count keep their selected values.

Active batches lock the preset controls. Start freezes the actual duration; Resume retains its frozen Plan independently of later library edits. AUTO still disables Cookie Relay. With Relay ON, the profile predicts the first runner’s duration; only fresh visual proof authorizes Relay input.

Fixed Custom fractional-value truncation/invalid-entry errors, completed-batch Telegram RUN confirmation using the previous profile, and Relay watchdog/Stop/Pause races during final blocking dispatch guards. Telegram STATUS and RUN confirmation show seconds. Pending Relay intents keep their never-replay lock.

Validation: **1,198 passed / 17 skipped (1,215 total)**. Real Linux Tk Save/Select/Edit/Delete/Reopen and locked-state checks passed. Signed upgrades from v0.18.13–v0.18.16 preserve nine runtime files each byte-for-byte, including saved timing presets. All 146 package hashes match the reviewed source. The 63 compiled profile/Boost/loop/Relay configurations retain exact v0.18.16 config and Plan identities.

Windows fonts, native Windows/LDPlayer input timing and game acceptance remain unverified. Human Verification, foreground, geometry, freshness and replay protections remain; Heart Sender input and runtime treasure/item reading policy are unchanged.

Existing installations: open **Settings → CHECK UPDATE**, stop workers, then close the Controller when installation is eligible. Active checkpoints defer installation; do not Reset a batch merely to install this update. Runtime state, statistics, sessions and historical rewards are retained.

ZIP SHA-256: `61aaa7b253669a10ed021a18bdae8dd2c5ef136a7b58f4e90d69b26509e83e5a`.

## v0.18.0 (initial release)

1. Download the ZIP from the [v0.18.0 release](https://github.com/balltro/AxiomVision-Releases/releases/tag/v0.18.0).
2. Close the Controller and game workers. Back up the existing installation, extract the ZIP over the same folder without deleting runtime state, and run `RUN-SETUP-WINDOWS.bat` once.
3. Download `ENABLE-AXIOM-AUTO-UPDATE-WINDOWS.bat` from this repository. Place it beside `RUN-SETUP-WINDOWS.bat` and run it once to configure the signed feed.

The updater checks the feed in the background and installs only when both Universal and Heart have no active worker or checkpoint. A running continuous batch is never paused or reset for an update. A failed package swap restores backed-up code files.

The signing private key is not stored in this repository or any release asset. `updates.json` is signed; release archive and every included file must match its signed hashes.
