from loguru import logger
from PySide6 import QtWidgets as qw
from utils import *

from .col import col


def card(
    title: str,
    widget_content: qw.QWidget,
    subtitle: str = None,
) -> qw.QFrame:
    """Wraps any chart or table inside a structured modern card frame."""
    crad_frame = qw.QFrame()
    
    set_style(
        crad_frame,
        Style(
            background_color=Color.FOUR,
            border_radius="12px",
            border=f"1px solid {Color.THREE}",
        ),
    )

    crad_frame.setSizePolicy(
        qw.QSizePolicy.Expanding,
        qw.QSizePolicy.Expanding,
    )

    title_label = qw.QLabel(title)

    widgets = [title_label]

    set_style(title_label, Style(
        font_size="15px",
        font_weight="700",
        color=Color.NINE,
        border="none",
        background_color="transparent",
    ))

    if subtitle:
        sub_label = qw.QLabel(subtitle)

        set_style(
            sub_label,
            Style(
                font_size="11px",
                color=Color.FIFE,
                border="none",
                background_color="transparent",
            ),
        )

        widgets.append(sub_label)
    
    header_layout = col(*widgets, margin=Margin(18, 14, 18, 4), spacing=2)

    content_layout = col(widget_content, margin=Margin(12, 4, 12, 12))

    crad_col = col(header_layout, content_layout, parent=crad_frame)
    
    return crad_col
