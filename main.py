import sys
from PySide6 import QtWidgets as qw

from utils import *
import widgets as wg
from pages.home import home


if __name__ == "__main__":
    app = qw.QApplication([])


    tabs = qw.QTabWidget()

    tabs.addTab(home(), "Home")

    tabs.resize(800, 600)
    tabs.show()

    sys.exit(app.exec())
