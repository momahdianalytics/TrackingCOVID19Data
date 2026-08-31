from PySide6 import QtWidgets as qw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
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
    sns.set_theme(
        style="whitegrid",
        rc={
            "figure.facecolor": "#FFFFFF",
            "axes.facecolor": "#FFFFFF",
            "axes.edgecolor": "#E2E8F0",
            "grid.color": "#F1F5F9",
            "grid.linestyle": "--",
            "text.color": "#1E293B",
            "axes.labelcolor": "#475569",
            "xtick.color": "#64748B",
            "ytick.color": "#64748B",
            "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Arial"],
        }
    )

    fig = Figure(dpi=100)
    fig.patch.set_facecolor("#FFFFFF")
    ax = fig.add_subplot(111)

    if title:
        ax.set_title(title, fontsize=12, fontweight="bold", color="#00465C", pad=12)

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

    fig.tight_layout()

    canvas = FigureCanvas(fig)
    widget = col(canvas)

    if size is not None:
        widget.setFixedSize(size[0], size[1])

    logger.debug(f"ℹ️ Created plot widget with figure: {fig}")

    return widget