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
        Rule(
            'QWidget',
            Style(
                font_family="'Segoe UI', 'SF Pro Display', Roboto, Helvetica, Arial, sans-serif",
                font_size='14px',
                color=Color.FIRST,
            ),
        ),

        Rule(
            'QTabWidget::pane',
            Style(
                border=f'1px solid {Color.THIRD}',
                background_color=Color.FOURTH,
                border_radius='8px',
                top='-1px',
            ),
        ),

        Rule(
            'QTabBar::tab',
            Style(
                background_color=Color.FOURTH,
                color=Color.FIFTH,
                padding='10px 24px',
                margin_right='4px',
                border_top_left_radius='8px',
                border_top_right_radius='8px',
                font_weight='600',
                border=f'1px solid {Color.THIRD}',
                border_bottom='none',
            ),
        ),

        Rule(
            'QTabBar::tab:selected',
            Style(
                background_color='#0284C7',
                color='#FFFFFF',
                border_color='#0284C7',
            ),
        ),

        Rule(
            'QTabBar::tab:hover:!selected',
            Style(
                background_color='#334155',
                color='#F8FAFC',
            ),
        ),

        Rule(
            'QScrollArea',
            Style(
                border='none',
                background_color='transparent',
            ),
        ),

        Rule(
            'QScrollArea > QWidget > QWidget',
            Style(
                background_color='transparent',
            ),
        ),

        Rule(
            'QScrollBar:vertical',
            Style(
                background_color='#0F172A',
                width='10px',
                margin='0px',
                border_radius='5px',
            ),
        ),

        Rule(
            'QScrollBar::handle:vertical',
            Style(
                background_color='#334155',
                min_height='20px',
                border_radius='5px',
            ),
        ),

        Rule(
            'QScrollBar::handle:vertical:hover',
            Style(
                background_color='#475569',
            ),
        ),

        Rule(
            'QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical',
            Style(
                height='0px',
            ),
        ),
    )


    window = qw.QMainWindow()

    set_style(window, Style(
        background_color=Color.SECOND,
    ))

    logger.add("logs/main.log", level="DEBUG", rotation="1 MB", encoding="utf-8", enqueue=True)

# ==============================================================
# Tabs widget
# ==============================================================
    tabs = qw.QTabWidget()
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