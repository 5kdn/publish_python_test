"""GUI アプリケーションの起動手順を提供する。"""

from publish_python.message_factory import build_greeting_message
from publish_python.tkinter_infrastructure import create_window, start_event_loop


def run_application() -> None:
    """画面へメッセージを表示する GUI アプリケーションを起動する。"""
    message = build_greeting_message()
    window = create_window(message)
    start_event_loop(window)
