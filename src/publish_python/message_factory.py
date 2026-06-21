"""画面表示用のメッセージを組み立てる。"""

from publish_python.view_model import GreetingMessage


def build_greeting_message() -> GreetingMessage:
    """Hello World を表示するメッセージを生成する。"""
    return GreetingMessage(
        window_title="Hello App",
        label_text="Hello World",
    )
