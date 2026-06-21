"""GUI アプリケーション起動経路の E2E テストを提供する。"""

import unittest
from unittest.mock import patch

from publish_python.main import main


class MainE2ETest(unittest.TestCase):
    """エントリポイントからの起動経路を検証する。"""

    @patch("publish_python.main.run_application")
    def test_main_starts_application(self, run_application_mock) -> None:
        """エントリポイントがアプリケーション起動処理を呼び出す。"""
        main()

        run_application_mock.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
