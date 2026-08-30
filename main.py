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

    logger.add("logs/main.log", level="DEBUG", rotation="1 MB", encoding="utf-8", enqueue=True)


    tabs = qw.QTabWidget()
    tabs.addTab(home(), "Home")


    widget = wg.col(
        wg.kpi_card((
            {"label": "😷 \nTotal Confirmed", "value": df["Confirmed"].sum()},
            {"label": "💀 \nTotal Deaths", "value": df["Deaths"].sum()},
            {"label": "🩺 \nTotal Recovered", "value": df["Recovered"].sum()},
            {"label": "🧪 \nTotal Active", "value": df["Active"].sum()},
        )),
        tabs,
    )

    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()