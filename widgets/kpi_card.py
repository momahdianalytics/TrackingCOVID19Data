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
            # Non-numeric KPI values (e.g. strings) previously crashed here.
            value_text = str(value)

        kpi_label = qw.QLabel(f"{kpi['label']}", alignment=CENTER)
        kpi_value = qw.QLabel(value_text, alignment=CENTER)
        set_style(kpi_label, Style(
            background_color=Color.FIRST,
            border=f"1px solid {Color.SECOND}",
            border_radius="5px",
            padding="5px",
        ))
        set_style(kpi_value, Style(
            background_color=Color.SECOND,
            border=f"1px solid {Color.FIRST}",
            border_radius="5px",
            padding="5px",
        ))
        kpi_widget = col(
            kpi_label,
            kpi_value,
        )
        kpi_widget.setFixedWidth(170)
        kpi_widgets.append(kpi_widget)

    widget = row(*kpi_widgets, alignment=CENTER, left_stretch=True, right_stretch=True, margin=Margin(all=10))

    set_style(widget, Style(
        font_size="20px",
    ))

    logger.debug(f"ℹ️  Created widget: {widget}")

    return widget
