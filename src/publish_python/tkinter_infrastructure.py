"""Tkinter を用いた GUI 構築を担当する。"""

import tkinter as tk

from publish_python.view_model import GreetingMessage
from publish_python.window_layout import DEFAULT_WINDOW_SIZE, to_geometry


def create_window(message: GreetingMessage) -> tk.Tk:
    """表示データから Tkinter のウィンドウを生成する。"""
    root = tk.Tk()
    root.title(message.window_title)
    root.geometry(to_geometry(DEFAULT_WINDOW_SIZE))

    label = tk.Label(root, text=message.label_text, padx=24, pady=24)
    label.pack()

    return root


def start_event_loop(root: tk.Tk) -> None:
    """Tkinter のイベントループを開始する。"""
    root.mainloop()
