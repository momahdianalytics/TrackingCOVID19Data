from PySide6 import QtWidgets as qw
from loguru import logger

from .plot import plot
from .table import table
from .col import col


@logger.catch
def table_plot(func, data, title=None, **kwargs) -> qw.QWidget:
    """Combines a chart and a table for the same data into one widget."""

    plot_widget = plot(func=func, data=data, title=title, **kwargs)
    table_widget = table(data)

    if plot_widget is None or table_widget is None:
        logger.error("❌ Failed to create plot or table widget inside table_plot.")
        return qw.QWidget()

    combined_widget = col(
        plot_widget, table_widget
    )

    logger.debug("ℹ️ Created table_plot widget successfully.")
    return combined_widget
