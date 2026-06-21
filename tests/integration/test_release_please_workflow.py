"""release-please workflow 設定の結合テストを提供する。"""

import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = PROJECT_ROOT / ".github" / "workflows" / "release-please.yml"


class ReleasePleaseWorkflowIntegrationTest(unittest.TestCase):
    """GitHub Actions と release-please の接続設定を検証する。"""

    def test_workflow_uses_release_please_action_with_release_asset_upload(self) -> None:
        """workflow が release 作成後に Windows exe を添付する。"""
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("googleapis/release-please-action@v4", workflow)
        self.assertIn("token: ${{ secrets.RELEASE_PLEASE_PAT }}", workflow)
        self.assertIn("config-file: .release-please-config.json", workflow)
        self.assertIn("manifest-file: .release-please-manifest.json", workflow)
        self.assertIn("release_created: ${{ steps.release.outputs.release_created }}", workflow)
        self.assertIn("tag_name: ${{ steps.release.outputs.tag_name }}", workflow)
        self.assertIn("runs-on: windows-latest", workflow)
        self.assertIn("uses: actions/checkout@v6", workflow)
        self.assertIn('uses: actions/setup-python@v6', workflow)
        self.assertIn('python-version: "3.14"', workflow)
        self.assertIn("run: ./scripts/build_exe.ps1", workflow)
        self.assertIn('gh release upload "${{ needs.release-please.outputs.tag_name }}" "dist/publish-python.exe" --clobber', workflow)
        self.assertNotIn("setup-uv", workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("issues: write", workflow)
        self.assertIn("pull-requests: write", workflow)


if __name__ == "__main__":
    unittest.main()
