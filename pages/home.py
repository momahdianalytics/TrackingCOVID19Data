from PySide6 import QtWidgets as qw
import seaborn as sns

from utils import *
import widgets as wg
from df import df


def home():
    data = df.sort_values('Confirmed', ascending=False).head(10)

    def make_chart():
        return wg.table_plot(
            func=sns.barplot,
            data=data,
            title='تجربة',
            x='Confirmed',
            y='Country/Region',
            size=(700,500)
        )

    left_col = wg.col(
        *[make_chart() for _ in range(3)],
        alignment=CENTER,
    )

    right_col = wg.col(
        *[make_chart() for _ in range(4)],
        alignment=CENTER,
    )

    widget = wg.row(
        left_col,
        right_col,
        alignment=CENTER,
        scrollable=True
    )

    return widget
