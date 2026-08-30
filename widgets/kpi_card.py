from PySide6 import QtWidgets as qw
from loguru import logger


from utils import *
from .row import row


@logger.catch
def kpi_card(data:tuple) -> qw.QWidget:
    widget = qw.QWidget()

    kpi_lables = []

    for kpi in data:
        kpi_lables.append(qw.QLabel(f"{kpi['label']}: {kpi['value'].round(2)}", alignment=CENTER))

    widget.setLayout(row(*kpi_lables, alignment=CENTER, left_stretch=True, right_stretch=True, margin=Margin(all=10)))

    set_style(widget, Style(
        font_size="20px",
    ))
    
    logger.debug(f"ℹ️  Created widget: {widget}")

    return widget