from PySide6 import QtWidgets as qw


def button(text, onclick:callable, size=None) -> qw.QPushButton:
    push_button = qw.QPushButton(
        text=text
    )
    push_button.clicked.connect(onclick)
    if size:
        push_button.setFixedSize(*size)
    return push_button