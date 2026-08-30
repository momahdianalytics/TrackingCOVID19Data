from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from loguru import logger
import seaborn as sns

@logger.catch
def plot(g:sns.FacetGrid, size=None) -> FigureCanvas:
    if size is not None:
        g.figure.set_size_inches(*size)

    logger.debug(f"ℹ️  Created widget: {g}")
    
    return FigureCanvas(g.figure)

