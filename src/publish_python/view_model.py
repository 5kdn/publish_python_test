"""GUI 表示に必要なデータ表現を定義する。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GreetingMessage:
    """GUI へ表示する文言を保持する。"""

    window_title: str
    label_text: str
