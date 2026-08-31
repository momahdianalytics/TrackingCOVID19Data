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
            title='Top Confirmed Cases',
            x='Confirmed',
            y='Country/Region',
            palette="crest",
            size=(520, 380)
        )

    left_col = wg.col(
        *[make_chart() for _ in range(2)],
        alignment=CENTER,
        spacing=20,
        margin=Margin(all=10)
    )

    right_col = wg.col(
        *[make_chart() for _ in range(2)],
        alignment=CENTER,
        spacing=20,
        margin=Margin(all=10)
    )

    widget = wg.row(
        left_col,
        right_col,
        alignment=CENTER,
        spacing=20,
        margin=Margin(all=10),
        scrollable=True
    )

    return widget