"""GUI ウィンドウの寸法表現を提供する。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class WindowSize:
    """GUI ウィンドウの初期寸法を表現する。"""

    width_px: int
    height_px: int


DEFAULT_WINDOW_SIZE = WindowSize(width_px=600, height_px=400)


def to_geometry(size: WindowSize) -> str:
    """Tkinter へ渡す geometry 文字列へ変換する。"""
    return f"{size.width_px}x{size.height_px}"
