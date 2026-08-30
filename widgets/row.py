from PySide6 import QtWidgets as qw
from loguru import logger


@logger.catch
def row(*args, alignment=None, left_stretch=None, right_stretch=None, spacing=None, margin=None) -> qw.QWidget:

    layout = qw.QHBoxLayout()
    widget = qw.QWidget()
    widget.setLayout(layout)

    if left_stretch:
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

    if right_stretch:
        layout.addStretch()

    if spacing is not None:
        layout.setSpacing(spacing)

    if margin:
        if margin.all:
            widget.setContentsMargins(margin.all, margin.all, margin.all, margin.all)
        else:
            widget.setContentsMargins(*margin)

    logger.debug(f"ℹ️  Created widget: {widget} with layout: {layout}")
    
    return widget

