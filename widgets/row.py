from PySide6 import QtWidgets as qw


def row(*args, alignment=None, left_stretch=None, right_stretch=None, spacing=None, margin=None) -> qw.QHBoxLayout:

    hbox = qw.QHBoxLayout()

    if left_stretch:
        hbox.addStretch()

    for widget in args:
        if isinstance(widget, qw.QWidget):
            if alignment:
                hbox.addWidget(widget, alignment=alignment)
            else:
                hbox.addWidget(widget)
        if isinstance(widget, qw.QLayout):
            hbox.addLayout(widget)

    if right_stretch:
        hbox.addStretch()

    if spacing is not None:
        hbox.setSpacing(spacing)

    if margin:
        if margin.all:
            hbox.setContentsMargins(margin.all, margin.all, margin.all, margin.all)
        else:
            hbox.setContentsMargins(*margin)

    return hbox

