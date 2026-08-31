from PySide6 import QtWidgets as qw
import pandas as pd
from loguru import logger


@logger.catch
def table(data: pd.DataFrame | pd.Series, size=None) -> qw.QTableWidget:
    tbl = qw.QTableWidget()

    if isinstance(data, pd.Series):
        tbl.setRowCount(len(data))
        tbl.setColumnCount(2)
        tbl.setHorizontalHeaderLabels([data.index.name or "Index", data.name or "Value"])

        for i, (idx, val) in enumerate(data.items()):
            tbl.setItem(i, 0, qw.QTableWidgetItem(str(idx)))
            tbl.setItem(i, 1, qw.QTableWidgetItem(str(val)))

    elif isinstance(data, pd.DataFrame):
        tbl.setRowCount(len(data))
        tbl.setColumnCount(len(data.columns))

        tbl.setHorizontalHeaderLabels([str(col) for col in data.columns])
        tbl.setVerticalHeaderLabels([str(idx) for idx in data.index])

        for i in range(len(data)):
            for j in range(len(data.columns)):
                item_text = str(data.iat[i, j])
                tbl.setItem(i, j, qw.QTableWidgetItem(item_text))
    else:
        raise TypeError(f"Unsupported data type: {type(data)} Only pd.DataFrame and pd.Series are supported")

    tbl.setAlternatingRowColors(True)
    tbl.horizontalHeader().setSectionResizeMode(qw.QHeaderView.Stretch)
    tbl.verticalHeader().setVisible(False)
    tbl.setShowGrid(False)

    tbl.setStyleSheet("""
        QTableWidget {
            background-color: #FFFFFF;
            alternate-background-color: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            color: #1E293B;
            selection-background-color: #E0F2FE;
            selection-color: #0369A1;
        }
        QHeaderView::section {
            background-color: #00465C;
            color: #FFFFFF;
            padding: 8px;
            border: none;
            font-weight: bold;
            font-size: 13px;
        }
    """)

    if size is not None:
        tbl.setFixedSize(*size)

    logger.debug(f"ℹ️  Created widget: {tbl}")

    return tbl