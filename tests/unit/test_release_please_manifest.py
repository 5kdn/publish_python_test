"""release-please マニフェスト設定の単体テストを提供する。"""

import json
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = PROJECT_ROOT / ".release-please-manifest.json"


class ReleasePleaseManifestUnitTest(unittest.TestCase):
    """release-please のバージョン追跡設定を検証する。"""

    def test_manifest_tracks_root_package_version(self) -> None:
        """ルートパッケージの初期バージョンを保持する。"""
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

        self.assertEqual(manifest, {".": "0.1.0"})


if __name__ == "__main__":
    unittest.main()
