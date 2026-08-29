from PySide6 import QtWidgets as qw
import pandas as pd

import pandas as pd
import PySide6.QtWidgets as qw


def table(data: pd.DataFrame | pd.Series, size=None) -> qw.QTableWidget:
    table = qw.QTableWidget()

    # Handle pd.Series
    if isinstance(data, pd.Series):
        # A Series is 1D: Rows = length of series, Columns = 2 (Index + Value)
        table.setRowCount(len(data))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels([data.index.name or "Index", data.name or "Value"])

        for i, (idx, val) in enumerate(data.items()):
            table.setItem(i, 0, qw.QTableWidgetItem(str(idx)))
            table.setItem(i, 1, qw.QTableWidgetItem(str(val)))

    # Handle pd.DataFrame
    elif isinstance(data, pd.DataFrame):
        table.setRowCount(len(data))
        table.setColumnCount(len(data.columns))

        # Set the column headers
        table.setHorizontalHeaderLabels([str(col) for col in data.columns])
        # Set the row index labels
        table.setVerticalHeaderLabels([str(idx) for idx in data.index])

        # Use .iat for fast, positional coordinate lookups
        for i in range(len(data)):
            for j in range(len(data.columns)):
                item_text = str(data.iat[i, j])
                table.setItem(i, j, qw.QTableWidgetItem(item_text))
    else:
        raise TypeError(f"Unsupported data type: {type(data)} Only pd.DataFrame and pd.Series are supported")

    if size is not None:
        table.setFixedSize(*size)

    return table
