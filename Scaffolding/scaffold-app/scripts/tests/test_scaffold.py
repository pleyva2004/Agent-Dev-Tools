import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("scaffold", Path(__file__).resolve().parents[1] / "scaffold.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ScaffoldTests(unittest.TestCase):
    def test_mobile_customization_and_existing_root_preservation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            existing = root / "instruction.md"
            existing.write_text("keep me")
            app = module.scaffold(root, "mobile", name="MyApp", bundle_id="dev.example.myapp")
            self.assertEqual(existing.read_text(), "keep me")
            self.assertIn("name: MyApp", (app / "project.yml").read_text())
            self.assertIn("@testable import MyApp", (app / "Tests/CounterTests.swift").read_text())
            self.assertFalse(any("__APP_" in p.read_text() for p in app.rglob("*") if p.is_file()))
            self.assertEqual(json.loads((app / "scaffold.json").read_text())["bundleId"], "dev.example.myapp")
            with self.assertRaises(ValueError):
                module.scaffold(root, "mobile")

    def test_invalid_input_leaves_root_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            for args in ({"app_dir": "../escape"}, {"name": "bad name"}, {"bundle_id": "invalid"}, {"next_version": "latest"}):
                with self.assertRaises(ValueError):
                    module.scaffold(directory, "mobile", **args)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_symlink_destination_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "mobile").symlink_to(root / "missing")
            with self.assertRaises(ValueError):
                module.scaffold(root, "mobile")

    def test_web_failure_removes_staging_without_publishing(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(module.subprocess, "run", side_effect=subprocess.CalledProcessError(1, "npx")):
                with self.assertRaises(subprocess.CalledProcessError):
                    module.scaffold(directory, "web")
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_web_overlay_and_explicit_version(self):
        def fake_generator(command, check):
            app = Path(command[3])
            app.mkdir()
            (app / "package.json").write_text('{"scripts":{"dev":"next dev"}}')
            (app / "package-lock.json").write_text('{}')
            return subprocess.CompletedProcess(command, 0)

        with tempfile.TemporaryDirectory() as directory:
            with patch.object(module.subprocess, "run", side_effect=fake_generator) as run:
                app = module.scaffold(directory, "web", next_version="16.4.0")
            command = run.call_args.args[0]
            self.assertEqual(command[2], "create-next-app@16.4.0")
            self.assertIn("--disable-git", command)
            self.assertIn("--src-dir", command)
            self.assertEqual(json.loads((app / "package.json").read_text())["scripts"]["typecheck"], "tsc --noEmit")
            self.assertTrue((app / "src/app/api/health/route.ts").exists())
            self.assertIn("!.env.example", (app / ".gitignore").read_text())


if __name__ == "__main__":
    unittest.main()
