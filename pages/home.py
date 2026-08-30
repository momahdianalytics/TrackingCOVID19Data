from PySide6 import QtWidgets as qw

from utils import *
import widgets as wg


def home():

    msg = qw.QLabel("Hello World!")
    set_style(msg, Style(font_size="20px"))
    set_hover(msg, Style(color="red"))

    widget = wg.col(
        msg,
        margin=Margin(all=5),
        alignment=CENTER
    )

    set_style(widget, Style(font_size="20px"))

    return widget