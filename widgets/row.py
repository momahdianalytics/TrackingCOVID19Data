from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *

@logger.catch
def row(*args, alignment=None, left_stretch=None, right_stretch=None, spacing=None, margin=None, scrollable=False, size_policy=None, scroll_bar_style=None, scroll_bar_handle_style=None, scroll_bar_handle_hover_style=None) -> qw.QWidget:

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
            widget.setContentsMargins(margin.left, margin.top, margin.right, margin.bottom)

    if size_policy:
        widget.setSizePolicy(size_policy)

    if scrollable:
        # Previously this built a QScrollArea and then discarded it by
        # returning `widget` unchanged, so `scrollable=True` did nothing.
        scroll_area = qw.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        logger.debug(f"ℹ️  Created scrollable widget: {scroll_area} wrapping {widget}")
        set_style(scroll_area, 
            Rule('QScrollBar:vertical', scroll_bar_style),
            Rule('QScrollBar::handle:vertical', scroll_bar_handle_style),
            Rule('QScrollBar::handle:vertical:hover', scroll_bar_handle_hover_style),
            Rule('QScrollArea', Style(
                border='none',
                background_color='transparent',
            )),
            Rule(
                'QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical', Style(
                height='0px',
            )),
        )
        return scroll_area

    logger.debug(f"ℹ️  Created widget: {widget} with layout: {layout}")

    return widget
