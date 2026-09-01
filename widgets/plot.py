from PySide6 import QtWidgets as qw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import seaborn as sns
from loguru import logger

from .col import col
from utils import *


def _human_format(num, pos):
    """Formats large numbers into clean K/M notation (e.g. 1.5M, 250K)."""
    if abs(num) >= 1e6:
        return f'{num*1e-6:.1f}M'.replace('.0M', 'M')
    elif abs(num) >= 1e3:
        return f'{num*1e-3:.0f}K'
    return f'{num:,.0f}'


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
    sns.set_theme(
        style="whitegrid",
        rc={
            "figure.facecolor": Color.TEN,
            "axes.facecolor": Color.FOUR,
            "axes.edgecolor": Color.THREE,
            "grid.color": Color.ELEVEN,
            "grid.linestyle": "--",
            "text.color": Color.ONE,
            "axes.labelcolor": Color.FIFE,
            "xtick.color": Color.FIFE,
            "ytick.color": Color.FIFE,
            "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Arial"],
        }
    )

    fig = Figure(dpi=100)
    fig.patch.set_facecolor(Color.FOUR)
    ax = fig.add_subplot(111)

    if title:
        ax.set_title(title, fontsize=12, fontweight="bold", color=Color.NINE, pad=10)

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

    func(**plot_kwargs, legend=legend)

    # Format numeric axis to K/M format instead of scientific notation (1e6)
    formatter = ticker.FuncFormatter(_human_format)
    ax.xaxis.set_major_formatter(formatter)

    # Clean axes styling and typography
    ax.tick_params(labelsize=9)
    ax.set_xlabel(ax.get_xlabel(), fontsize=10, fontweight="600", labelpad=8)
    ax.set_ylabel(ax.get_ylabel(), fontsize=10, fontweight="600", labelpad=8)

    if ax.get_legend():
        ax.legend(
            fontsize=8,
            title_fontsize=7,
        )

    # Automatically adjust margins so text is never truncated
    fig.subplots_adjust(left=0.28, right=0.96, top=0.92, bottom=0.18)

    canvas = FigureCanvas(fig)
    canvas.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)
    canvas.updateGeometry()

    widget = col(canvas)
    widget.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)

    if size is not None:
        widget.setMinimumSize(size[0], size[1])

    logger.debug(f"ℹ️ Created plot widget with figure: {fig}")

    return widget