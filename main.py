import sys

from PySide6 import QtWidgets as qw
from loguru import logger

from utils import *
import widgets as wg
from pages.home import home
from df import df


@logger.catch
def main():
    app = qw.QApplication([])
    app.setStyle("Fusion")

    app.setStyleSheet("""
        QWidget {
            font-family: 'Segoe UI', 'SF Pro Display', Roboto, Helvetica, Arial, sans-serif;
            font-size: 14px;
            color: #1E293B;
        }
        QMainWindow {
            background-color: #F1F5F9;
        }
        QTabWidget::pane {
            border: 1px solid #CBD5E1;
            background-color: #FFFFFF;
            border-radius: 8px;
            top: -1px;
        }
        QTabBar::tab {
            background-color: #E2E8F0;
            color: #475569;
            padding: 10px 24px;
            margin-right: 4px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            font-weight: 600;
        }
        QTabBar::tab:selected {
            background-color: #0097C5;
            color: #FFFFFF;
        }
        QTabBar::tab:hover:!selected {
            background-color: #CBD5E1;
            color: #1E293B;
        }
        QScrollArea {
            border: none;
            background-color: transparent;
        }
        QScrollArea > QWidget > QWidget {
            background-color: transparent;
        }
    """)

    window = qw.QMainWindow()

    logger.add("logs/main.log", level="DEBUG", rotation="1 MB", encoding="utf-8", enqueue=True)

    tabs = qw.QTabWidget()
    tabs.addTab(home(), "Home")

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