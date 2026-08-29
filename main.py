import sys
from PySide6 import QtWidgets as qw

from utils import *
import widgets as wg


if __name__ == "__main__":
    app = qw.QApplication([])

    from pages import home

    tabs = wg.tabs(
        home.widget,
        size=(800, 600)
    )

    tabs.show()

    sys.exit(app.exec())
