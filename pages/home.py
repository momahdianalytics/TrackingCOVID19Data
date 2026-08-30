from PySide6 import QtWidgets as qw

from utils import *
import widgets as wg


def home():

    widget = wg.col(
        qw.QLabel("Hello World!"),
        margin=Margin(all=5),
        alignment=CENTER
    )

    set_style(widget, Style(font_size="20px"))

    return widget