from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *


@logger.catch
def grid(items:tuple[tuple[qw.QWidget]], alignment=None, spacing=None, margin:Margin=None) -> qw.QWidget:

    layout = qw.QGridLayout()
    widget = qw.QWidget()
    widget.setLayout(layout)

    for i, col in enumerate(items):
        for j, item in enumerate(col):
            if item is 0:
                continue
            elif isinstance(item, qw.QWidget):
                if alignment:
                    layout.addWidget(item, j, i, alignment=alignment)
                else:
                    layout.addWidget(item, j, i)
            elif isinstance(item, qw.QLayout):
                layout.addLayout(item, j, i)
            else:
                raise ValueError(f"Unsupported item type: {type(item)}")
        
    if spacing:
        layout.setSpacing(spacing)

    if margin:
        if margin.all:
            widget.setContentsMargins(margin.all, margin.all, margin.all, margin.all)
        else:
            widget.setContentsMargins(*margin)

    logger.debug(f"ℹ️  Created widget: {widget} with layout: {layout}")
    
    return widget

