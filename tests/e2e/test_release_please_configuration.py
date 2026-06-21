"""release-please 設定一式の E2E テストを提供する。"""

import json
import tomllib
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / ".release-please-config.json"
MANIFEST_PATH = PROJECT_ROOT / ".release-please-manifest.json"
PYPROJECT_PATH = PROJECT_ROOT / "pyproject.toml"


class ReleasePleaseConfigurationE2ETest(unittest.TestCase):
    """リリース設定がアプリ設定と整合することを検証する。"""

    def test_release_please_configuration_matches_project_metadata(self) -> None:
        """release-please 設定が pyproject の公開情報と一致する。"""
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        pyproject = tomllib.loads(PYPROJECT_PATH.read_text(encoding="utf-8"))

        self.assertEqual(config["packages"]["."]["package-name"], pyproject["project"]["name"])
        self.assertEqual(config["packages"]["."]["release-type"], "python")
        self.assertEqual(manifest["."], pyproject["project"]["version"])


if __name__ == "__main__":
    unittest.main()
