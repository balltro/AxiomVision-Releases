"""Stopped blocked Universal checkpoints must retain controller authority."""
from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import visionstudio_controller as controller
import visionstudio_controller_state as control
import test_recovery_field_regression as field


class RecoveryControllerBoundaryTests(unittest.TestCase):
    def scene(self, root):
        fixture = field.RecoveryFieldRegressionTests()
        server, session, desktop = fixture.field_scene(root)
        self.addCleanup(server.close)
        return session, session.checkpoint_payload(status="blocked")

    def test_blocked_universal_remains_resumable_without_changing_its_ledger(self):
        with tempfile.TemporaryDirectory() as tmp:
            session, cp = self.scene(Path(tmp))
            before = copy.deepcopy(cp)
            self.assertTrue(controller.checkpoint_is_resumable(session.mission, cp))
            self.assertEqual(cp, before)

    def test_stop_keeps_resume_available_and_heart_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            session, cp = self.scene(Path(tmp))
            state = control.patch_state(Path(tmp) / "state.json", desired_state="stopped", worker={"status": "stopped", "pid": None})
            resumable = controller.checkpoint_is_resumable(session.mission, cp)
            availability = controller.action_availability("stopped", worker_active=False, checkpoint_resumable=resumable)
            self.assertTrue(availability.resume)
            self.assertIsNotNone(controller.universal_runtime_conflict(state, worker_active=False, checkpoint_resumable=resumable))

    def test_start_from_stopped_requires_archive_before_replacing_blocked_checkpoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            session, cp = self.scene(root)
            path = root / "state.json"
            control.patch_state(path, desired_state="stopped", worker={"status": "stopped", "pid": None})
            app = SimpleNamespace(control_path=path, mission_path=session.mission_path,
                _validate_ready=mock.Mock(return_value=session.mission), _requested_loops=lambda: 1,
                _stats=lambda: ({}, cp), _heart_conflict_for_universal=lambda: None,
                _worker_active=lambda: False,
                _capture_current_geometry=mock.Mock(return_value={"bounds": list(session.fixed_geometry_bounds), "source": "test", "captured_at": "now"}),
                _launch_worker=mock.Mock(), _archive_runtime_batch=mock.Mock(),
                _retire_open_review_verification=mock.Mock(),
                telegram_enabled=SimpleNamespace(get=lambda: False),
                _boost_config=lambda: {"random_mode": "off", "random_target": "Double Coins"},
                _run_profile=lambda: {"mode": "custom", "expected_seconds": 30},
                _universal_config=lambda: session.universal_config)
            with mock.patch.object(controller, "runtime_mission", return_value=session.mission):
                result = controller.VisionStudioController._execute_start_run(app, archive_resumable_checkpoint=False)
            self.assertFalse(result.ok)
            self.assertEqual(result.code, "checkpoint_resumable")
            app._capture_current_geometry.assert_not_called()
            app._launch_worker.assert_not_called()
            self.assertIsNotNone(cp["pending_action_intent"])

    def test_reset_stopped_completed_unknown_and_final_stage_are_not_resumable(self):
        with tempfile.TemporaryDirectory() as tmp:
            session, cp = self.scene(Path(tmp))
            for status in ("reset", "stopped", "completed", "unknown"):
                changed = copy.deepcopy(cp); changed["status"] = status
                with self.subTest(status=status):
                    self.assertFalse(controller.checkpoint_is_resumable(session.mission, changed))
            changed = copy.deepcopy(cp)
            changed.update(current_stage_id=session.mission["steps"][-1]["id"], current_stage_phase="completed")
            self.assertFalse(controller.checkpoint_is_resumable(session.mission, changed))

    def test_blocked_legacy_foreign_plan_and_unknown_stage_have_no_resume_authority(self):
        with tempfile.TemporaryDirectory() as tmp:
            session, cp = self.scene(Path(tmp))
            for mutation in ("legacy", "contract", "stage", "phase"):
                changed = copy.deepcopy(cp)
                if mutation == "legacy": changed["mission_source"] = "file"
                elif mutation == "contract": changed["mission_contract_sha256"] = "c" * 64
                elif mutation == "stage": changed["current_stage_id"] = "unknown-stage"
                else: changed["current_stage_phase"] = "unknown-phase"
                with self.subTest(mutation=mutation):
                    self.assertFalse(controller.checkpoint_is_resumable(session.mission, changed))


if __name__ == "__main__":
    unittest.main()
