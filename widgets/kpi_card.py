from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *
from .row import row
from .col import col


@logger.catch
def kpi_card(data: tuple) -> qw.QWidget:

    kpi_widgets = []

    for kpi in data:
        value = kpi["value"]

        try:
            value_text = f"{value:,.0f}"
        except (ValueError, TypeError):
            value_text = str(value)

        kpi_label = qw.QLabel(
            kpi["label"],
            alignment=CENTER,
        )

        kpi_value = qw.QLabel(
            value_text,
            alignment=CENTER,
        )

        set_style(
            kpi_label,
            Style(
                background_color="#1E293B",
                color="#94A3B8",
                font_size="13px",
                font_weight="600",
                padding="8px",
                border_top_left_radius="10px",
                border_top_right_radius="10px",
                border="1px solid #334155",
                border_bottom="none",
            ),
        )

        set_style(
            kpi_value,
            Style(
                background_color="#0F172A",
                color="#38BDF8",
                font_size="18px",
                font_weight="bold",
                padding="8px",
                border_bottom_left_radius="10px",
                border_bottom_right_radius="10px",
                border="1px solid #334155",
            ),
        )

        kpi_widget = col(
            kpi_label,
            kpi_value,
            spacing=0,
        )

        kpi_widget.setFixedWidth(200)
        kpi_widgets.append(kpi_widget)

    widget = row(
        *kpi_widgets,
        alignment=CENTER,
        left_stretch=True,
        right_stretch=True,
        spacing=15,
        margin=Margin(all=10),
    )

    logger.debug(f"ℹ️  Created widget: {widget}")

    return widget
