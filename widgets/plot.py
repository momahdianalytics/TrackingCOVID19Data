from PySide6 import QtWidgets as qw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from loguru import logger
import matplotlib.pyplot as plt

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
    size=(5, 4),
) -> qw.QWidget:
    # 1. إنشاء الـ Figure والـ Axes
    fig, ax = plt.subplots(figsize=size)

    # 2. تعيين العنوان إذا وجد
    if title:
        ax.set_title(title)

    # 3. جمع الوسائط المطلوبة لتمريرها لدالة الرسم
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

    # 4. تنفيذ دالة الرسم
    func(**plot_kwargs)

    # 5. التعامل مع مفتاح الـ legend إن وجد
    if not legend and ax.get_legend():
        ax.get_legend().remove()

    # 6. ربط الرسم بـ PySide6 Canvas
    canvas = FigureCanvas(fig)
    
    if size is not None:
        canvas.setFixedSize(size[0]*100, size[1]*100) # تحويل الأبعاد إلى بكسل تقريبي أو إزالة التقييد الثابت إذا سبب مشاكل

    logger.debug(f"ℹ️ Created plot widget with figure: {fig}")

    return canvas