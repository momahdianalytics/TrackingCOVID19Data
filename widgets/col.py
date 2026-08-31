from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *


@logger.catch
def col(*args, alignment=None, top_stretch=None, bottom_stretch=None, spacing=None, margin: Margin = None, scrollable=False) -> qw.QWidget:

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

    if scrollable:
        # Previously this built a QScrollArea and then discarded it by
        # returning `widget` unchanged, so `scrollable=True` did nothing.
        scroll_area = qw.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        logger.debug(f"ℹ️  Created scrollable widget: {scroll_area} wrapping {widget}")
        return scroll_area

    logger.debug(f"ℹ️  Created widget: {widget} with layout: {layout}")

    return widget
