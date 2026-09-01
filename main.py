import sys

from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *
import widgets as wg
from pages.tab_1 import tab_1
from pages.tab_2 import tab_2
from df import df


@logger.catch
def main():
    app = qw.QApplication([])
    app.setStyle("Fusion")

    set_style(
        app,
        Rule('QWidget', Style(
            font_family="'Segoe UI', 'SF Pro Display', Roboto, Helvetica, Arial, sans-serif",
            font_size='14px',
            color=Color.ONE,
    )))


    window = qw.QMainWindow()

    set_style(window, Style(
        background_color=Color.TOW,
    ))

    logger.add("logs/main.log", level="DEBUG", rotation="1 MB", encoding="utf-8", enqueue=True)

# ==============================================================
# Tabs widget
# ==============================================================
    tabs = wg.tab(
        pane_style=Style(
            border=f'1px solid {Color.THREE}',
            background_color=Color.FOUR,
            border_radius='8px',
            top='-1px',
        ),
        tab_style=Style(
            background_color=Color.FOUR,
            color=Color.FIFE,
            padding='10px 24px',
            margin_right='4px',
            border_top_left_radius='8px',
            border_top_right_radius='8px',
            font_weight='600',
            border=f'1px solid {Color.THREE}',
            border_bottom='none',
        ),
        tab_selected_style=Style(
            background_color=Color.SIX,
            color=Color.SEVEN,
            border_color=Color.SIX,
        ),
        tab_hover_style=Style(
            background_color=Color.THREE,
            color=Color.ONE,
        ),
    )
    tabs.addTab(tab_1(), "Tab 1")
    tabs.addTab(tab_2(), "Tab 2")
# ==============================================================

    central_widget = wg.col(
        wg.kpi_card((
            {"label": "😷 \nTotal Confirmed", "value": df["Confirmed"].sum()},
            {"label": "💀 \nTotal Deaths", "value": df["Deaths"].sum()},
            {"label": "🩺 \nTotal Recovered", "value": df["Recovered"].sum()},
            {"label": "🧪 \nTotal Active", "value": df["Active"].sum()},
        )),
        tabs,
        spacing=15,
        margin=Margin(all=15)
    )

    window.setCentralWidget(central_widget)

    window.resize(1150, 750)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()