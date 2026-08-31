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
            "background-color: #1E293B; color: #94A3B8; "
            "font-size: 13px; font-weight: 600; padding: 8px; "
            "border-top-left-radius: 10px; border-top-right-radius: 10px; "
            "border: 1px solid #334155; border-bottom: none;"
        )

        kpi_value.setStyleSheet(
            "background-color: #0F172A; color: #38BDF8; "
            "font-size: 18px; font-weight: bold; padding: 8px; "
            "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; "
            "border: 1px solid #334155;"
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