from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *
from .row import row
from .col import col


@logger.catch
def kpi_card(data: tuple) -> qw.QWidget:

    kpi_widgets = []

    for kpi in data:
        value = kpi['value']
        try:
            value_text = f"{value:,.0f}"
        except (ValueError, TypeError):
            value_text = str(value)

        kpi_label = qw.QLabel(f"{kpi['label']}", alignment=CENTER)
        kpi_value = qw.QLabel(value_text, alignment=CENTER)

        kpi_label.setStyleSheet(
            "background-color: #FFFFFF; color: #475569; "
            "font-size: 13px; font-weight: 600; padding: 8px; "
            "border-top-left-radius: 10px; border-top-right-radius: 10px; "
            "border: 1px solid #E2E8F0; border-bottom: none;"
        )

        kpi_value.setStyleSheet(
            f"background-color: {Color.FIRST}; color: #FFFFFF; "
            "font-size: 18px; font-weight: bold; padding: 8px; "
            "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; "
            f"border: 1px solid {Color.FIRST};"
        )

        kpi_widget = col(
            kpi_label,
            kpi_value,
            spacing=0
        )
        kpi_widget.setFixedWidth(200)
        kpi_widgets.append(kpi_widget)

    widget = row(*kpi_widgets, alignment=CENTER, left_stretch=True, right_stretch=True, spacing=15, margin=Margin(all=10))

    logger.debug(f"ℹ️  Created widget: {widget}")

    return widget