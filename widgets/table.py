from PySide6 import QtWidgets as qw, QtCore as qc
import pandas as pd
from loguru import logger

from utils import *


@logger.catch
def table(data: pd.DataFrame | pd.Series, size=None) -> qw.QTableWidget:
    tbl = qw.QTableWidget()

    if isinstance(data, pd.Series):
        tbl.setRowCount(len(data))
        tbl.setColumnCount(2)

        tbl.setHorizontalHeaderLabels([
            data.index.name or "Index",
            data.name or "Value",
        ])

        for i, (idx, val) in enumerate(data.items()):
            tbl.setItem(i, 0, qw.QTableWidgetItem(str(idx)))

            val_text = (
                f"{val:,.0f}"
                if isinstance(val, (int, float))
                else str(val)
            )

            item = qw.QTableWidgetItem(val_text)
            item.setTextAlignment(qc.Qt.AlignRight | qc.Qt.AlignVCenter)

            tbl.setItem(i, 1, item)

    elif isinstance(data, pd.DataFrame):
        tbl.setRowCount(len(data))
        tbl.setColumnCount(len(data.columns))

        tbl.setHorizontalHeaderLabels([
            str(col) for col in data.columns
        ])

        tbl.setVerticalHeaderLabels([
            str(idx) for idx in data.index
        ])

        for i in range(len(data)):
            for j in range(len(data.columns)):
                val = data.iat[i, j]

                if isinstance(val, (int, float)):
                    val_text = f"{val:,.0f}"

                    item = qw.QTableWidgetItem(val_text)
                    item.setTextAlignment(
                        qc.Qt.AlignRight | qc.Qt.AlignVCenter
                    )
                else:
                    item = qw.QTableWidgetItem(str(val))
                    item.setTextAlignment(
                        qc.Qt.AlignLeft | qc.Qt.AlignVCenter
                    )

                tbl.setItem(i, j, item)

    else:
        raise TypeError(
            f"Unsupported data type: {type(data)} "
            "Only pd.DataFrame and pd.Series are supported"
        )

    tbl.setAlternatingRowColors(True)
    tbl.horizontalHeader().setSectionResizeMode(qw.QHeaderView.Stretch)
    tbl.verticalHeader().setVisible(False)
    tbl.setShowGrid(False)
    tbl.setEditTriggers(qw.QAbstractItemView.NoEditTriggers)
    tbl.setSelectionBehavior(qw.QAbstractItemView.SelectRows)

    set_style(
        tbl,
        Style(
            background_color=Color.FOUR,
            alternate_background_color=Color.TWELFE,
            border=f"1px solid {Color.THREE}",
            border_radius="8px",
            color=Color.ONE,
            font_size="13px",
            selection_background_color=Color.THIRDTEEN,
            selection_color=Color.SEVEN,
        ),

        Rule(
            "QHeaderView::section",
            Style(
                background_color=Color.TOW,
                color=Color.NINE,
                padding="8px 10px",
                border="none",
                border_bottom=F"1px solid {Color.THREE}",
                font_weight="bold",
                font_size="12px",
            ),
        ),
    )

    tbl.setSizePolicy(
        qw.QSizePolicy.Expanding,
        qw.QSizePolicy.Expanding,
    )

    if size is not None:
        tbl.setMinimumSize(*size)

    logger.debug(f"ℹ️  Created table widget: {tbl}")

    return tbl