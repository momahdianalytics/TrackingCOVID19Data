from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *


@logger.catch
def tab(
    pane_style: Style=None, 
    tab_style: Style=None, 
    tab_selected_style: Style=None,
    tab_hover_style: Style=None,
) -> qw.QTabWidget:

    widget = qw.QTabWidget()

    set_style(widget, 
        Rule('QTabWidget::pane', pane_style),
        Rule('QTabBar::tab', tab_style),
        Rule('QTabBar::tab:selected', tab_selected_style),
        Rule('QTabBar::tab:hover:!selected', tab_hover_style),
    )

    return widget
