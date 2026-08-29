from PySide6 import QtWidgets as qw

from utils import *


def tabs(*args, margin:Margin=None, size=None) -> qw.QTabWidget:

    tabs = qw.QTabWidget()

    for widget in args:
        if isinstance(widget, qw.QWidget):
            tabs.addTab(widget, widget.property("page_name"))
        else:
            raise Exception(f"Widget {widget} is not a QWidget")

    if margin:
        if margin.all:
            tabs.setContentsMargins(margin.all, margin.all, margin.all, margin.all)
        else:
            tabs.setContentsMargins(*margin)

    if size:
        tabs.resize(*size)

    return tabs

