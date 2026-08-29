from PySide6 import QtWidgets as qw

from utils import *


def widget(layout:qw.QLayout, name) -> qw.QWidget:

    widget = qw.QWidget()
    widget.setLayout(layout)
    widget.setProperty("page_name", name)

    return widget

