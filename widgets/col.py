from PySide6 import QtWidgets as qw

from utils import *


def col(*args, alignment=None, top_stretch=None, bottom_stretch=None, spacing=None, margin:Margin=None) -> qw.QVBoxLayout:

    vbox = qw.QVBoxLayout()

    if top_stretch:
        vbox.addStretch()

    for widget in args:
        if isinstance(widget, qw.QWidget):
            if alignment:
                vbox.addWidget(widget, alignment=alignment)
            else:
                vbox.addWidget(widget)
        if isinstance(widget, qw.QLayout):
            vbox.addLayout(widget)

    if bottom_stretch:
        vbox.addStretch()

    if spacing:
        vbox.setSpacing(spacing)

    if margin:
        if margin.all:
            vbox.setContentsMargins(margin.all, margin.all, margin.all, margin.all)
        else:
            vbox.setContentsMargins(*margin)

    return vbox

