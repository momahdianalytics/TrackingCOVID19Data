from PySide6 import QtWidgets as qw
import pandas as pd
from loguru import logger


@logger.catch
def table(data: pd.DataFrame | pd.Series, size=None) -> qw.QTableWidget:
    table = qw.QTableWidget()

    if isinstance(data, pd.Series):
        table.setRowCount(len(data))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels([data.index.name or "Index", data.name or "Value"])

        for i, (idx, val) in enumerate(data.items()):
            table.setItem(i, 0, qw.QTableWidgetItem(str(idx)))
            table.setItem(i, 1, qw.QTableWidgetItem(str(val)))

    elif isinstance(data, pd.DataFrame):
        table.setRowCount(len(data))
        table.setColumnCount(len(data.columns))

        table.setHorizontalHeaderLabels([str(col) for col in data.columns])
        table.setVerticalHeaderLabels([str(idx) for idx in data.index])

        for i in range(len(data)):
            for j in range(len(data.columns)):
                item_text = str(data.iat[i, j])
                table.setItem(i, j, qw.QTableWidgetItem(item_text))
    else:
        raise TypeError(f"Unsupported data type: {type(data)} Only pd.DataFrame and pd.Series are supported")

    if size is not None:
        table.setFixedSize(*size)

    logger.debug(f"ℹ️  Created widget: {table}")

    return table
