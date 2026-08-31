from PySide6 import QtWidgets as qw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from loguru import logger

from .col import col


@logger.catch
def plot(
    func,
    title=None,
    data=None,
    legend=True,
    palette=None,
    kind=None,
    hue=None,
    x=None,
    y=None,
    size=None,
) -> qw.QWidget:
    # Use a standalone Figure (not plt.subplots()) so figures aren't
    # registered in pyplot's global state and never get garbage collected.
    fig = Figure()
    ax = fig.add_subplot(111)

    if title:
        ax.set_title(title)

    plot_kwargs = {'ax': ax}
    if data is not None:
        plot_kwargs['data'] = data
    if x is not None:
        plot_kwargs['x'] = x
    if y is not None:
        plot_kwargs['y'] = y
    if hue is not None:
        plot_kwargs['hue'] = hue
    if palette is not None:
        plot_kwargs['palette'] = palette
    if kind is not None:
        plot_kwargs['kind'] = kind

    func(**plot_kwargs)

    if not legend and ax.get_legend():
        ax.get_legend().remove()

    canvas = FigureCanvas(fig)
    widget = col(canvas)

    if size is not None:
        widget.setFixedSize(size[0], size[1])

    logger.debug(f"ℹ️ Created plot widget with figure: {fig}")

    return widget
