from PySide6 import QtWidgets as qw

from utils import *
import widgets as wg


layout = wg.col(
    qw.QLabel("Hello World!"),
)

widget = wg.widget(
    layout=layout,
    name="Home"
)

set_style(widget, Style(font_size="20px"))