"""window_layout モジュールの単体テストを提供する。"""

import unittest

from publish_python.window_layout import DEFAULT_WINDOW_SIZE, to_geometry


class WindowLayoutTest(unittest.TestCase):
    """ウィンドウ寸法表現を検証する。"""

    def test_to_geometry_returns_width_then_height(self) -> None:
        """初期ウィンドウ寸法を geometry 形式へ変換する。"""
        self.assertEqual(to_geometry(DEFAULT_WINDOW_SIZE), "600x400")


if __name__ == "__main__":
    unittest.main()
