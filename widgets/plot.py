from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns

def plot(g:sns.FacetGrid, size=None) -> FigureCanvas:
    if size is not None:
        g.figure.set_size_inches(*size)
    return FigureCanvas(g.figure)

