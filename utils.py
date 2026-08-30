from dataclasses import dataclass, fields
from PySide6 import QtCore as qc


CENTER = qc.Qt.AlignCenter
RIGHT = qc.Qt.AlignRight
LEFT = qc.Qt.AlignLeft
TOP = qc.Qt.AlignTop
BOTTOM = qc.Qt.AlignBottom

CENTER_COL = qc.Qt.AlignVCenter
CENTER_ROW = qc.Qt.AlignHCenter


@dataclass
class Style:
    background_color: str | None = None
    color: str | None = None
    border: str | None = None
    border_radius: str | None = None

    padding: str | None = None
    padding_top: str | None = None
    padding_right: str | None = None
    padding_bottom: str | None = None
    padding_left: str | None = None

    margin: str | None = None
    margin_top: str | None = None
    margin_right: str | None = None
    margin_bottom: str | None = None
    margin_left: str | None = None

    font_size: str | None = None
    font_weight: str | None = None

    def __str__(self) -> str:
        properties = []

        for field in fields(self):
            value = getattr(self, field.name)

            if value is not None:
                name = field.name.replace("_", "-")
                properties.append(f"{name}: {value};")

        return " ".join(properties)


@dataclass
class Rule:
    selector: str
    style: Style

    def __str__(self) -> str:
        return f"{self.selector} {{ {self.style} }}"


@dataclass
class Margin:
    left: int | None = None
    top: int | None = None
    right: int | None = None
    bottom: int | None = None
    all: int | None = None


def set_style(widget, style: Style) -> None:
    widget.setStyleSheet(str(style))