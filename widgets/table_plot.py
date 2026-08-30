from PySide6 import QtWidgets as qw
from loguru import logger
from .plot import plot
from .table import table
from .col import col

@logger.catch
def table_plot(func, data, title=None, **kwargs) -> qw.QWidget:
    """
    دالة تجمع بين عرض الرسم البياني والجدول الخاص بالبيانات
    """
    # 1. إنشاء عنصر الرسم البياني
    plot_widget = plot(func=func, data=data, title=title, **kwargs)
    
    # 2. إنشاء عنصر الجدول
    table_widget = table(data)
    
    # 3. التأكد من أن المخرجات ليست None لتجنب انهيار الـ grid لاحقاً
    if plot_widget is None or table_widget is None:
        logger.error("❌ Failed to create plot or table widget inside table_plot.")
        return qw.QWidget()

    # تصحيح المشكلة: تمرير العناصر مباشرة كـ arguments منفصلة وليست داخل Tuple
    combined_widget = col(
        plot_widget, table_widget
    )
    
    logger.debug(f"ℹ️ Created table_plot widget successfully.")
    return combined_widget