from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *


@logger.catch
def grid(items:tuple[tuple[qw.QWidget]], alignment=None, spacing=None, margin:Margin=None) -> qw.QWidget:

    layout = qw.QGridLayout()
    widget = qw.QWidget()
    widget.setLayout(layout)

    for i, row in enumerate(items):
        for j, item in enumerate(row):
            if item is 0:
                continue
            elif isinstance(item, qw.QWidget):
                if alignment:
                    layout.addWidget(item, i, j, alignment=alignment)
                else:
                    layout.addWidget(item, i, j)
            elif isinstance(item, qw.QLayout):
                layout.addLayout(item, i, j)
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

