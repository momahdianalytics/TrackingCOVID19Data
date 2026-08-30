from PySide6 import QtWidgets as qw

from utils import *


def col(*args, alignment=None, top_stretch=None, bottom_stretch=None, spacing=None, margin:Margin=None) -> qw.QWidget:

    layout = qw.QVBoxLayout()
    widget = qw.QWidget()
    widget.setLayout(layout)

    if top_stretch:
        layout.addStretch()

    for item in args:
        if isinstance(item, qw.QWidget):
            if alignment:
                layout.addWidget(item, alignment=alignment)
            else:
                layout.addWidget(item)
        elif isinstance(item, qw.QLayout):
                    layout.addLayout(item)
        else:
            raise ValueError(f"Unsupported item type: {type(item)}")
        
    if bottom_stretch:
        layout.addStretch()

    if spacing:
        layout.setSpacing(spacing)

    if margin:
        if margin.all:
            widget.setContentsMargins(margin.all, margin.all, margin.all, margin.all)
        else:
            widget.setContentsMargins(*margin)

    return widget

