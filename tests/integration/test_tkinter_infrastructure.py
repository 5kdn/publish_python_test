"""Tkinter インフラ層の結合テストを提供する。"""

import unittest
from unittest.mock import MagicMock, patch

from publish_python.tkinter_infrastructure import create_window
from publish_python.view_model import GreetingMessage


class CreateWindowIntegrationTest(unittest.TestCase):
    """Tkinter 連携を検証する。"""

    @patch("publish_python.tkinter_infrastructure.tk.Label")
    @patch("publish_python.tkinter_infrastructure.tk.Tk")
    def test_create_window_applies_title_geometry_and_label(
        self,
        tk_factory: MagicMock,
        label_factory: MagicMock,
    ) -> None:
        """生成したウィンドウへ初期表示設定を適用する。"""
        root = MagicMock()
        label = MagicMock()
        tk_factory.return_value = root
        label_factory.return_value = label
        message = GreetingMessage(window_title="title", label_text="hello")

        created = create_window(message)

        self.assertIs(created, root)
        root.title.assert_called_once_with("title")
        root.geometry.assert_called_once_with("600x400")
        label_factory.assert_called_once_with(root, text="hello", padx=24, pady=24)
        label.pack.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
