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
            color: #F8FAFC;
        }
        QMainWindow {
            background-color: #0F172A;
        }
        QTabWidget::pane {
            border: 1px solid #334155;
            background-color: #1E293B;
            border-radius: 8px;
            top: -1px;
        }
        QTabBar::tab {
            background-color: #1E293B;
            color: #94A3B8;
            padding: 10px 24px;
            margin-right: 4px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            font-weight: 600;
            border: 1px solid #334155;
            border-bottom: none;
        }
        QTabBar::tab:selected {
            background-color: #0284C7;
            color: #FFFFFF;
            border-color: #0284C7;
        }
        QTabBar::tab:hover:!selected {
            background-color: #334155;
            color: #F8FAFC;
        }
        QScrollArea {
            border: none;
            background-color: transparent;
        }
        QScrollArea > QWidget > QWidget {
            background-color: transparent;
        }
        QScrollBar:vertical {
            background-color: #0F172A;
            width: 10px;
            margin: 0px;
            border-radius: 5px;
        }
        QScrollBar::handle:vertical {
            background-color: #334155;
            min-height: 20px;
            border-radius: 5px;
        }
        QScrollBar::handle:vertical:hover {
            background-color: #475569;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
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