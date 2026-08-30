from PySide6 import QtWidgets as qw
import seaborn as sns

from utils import *
import widgets as wg
from df import df



def home():
    data = df.sort_values('Confirmed', ascending=False).head(10)

    widget = wg.grid((
        (
            wg.table_plot(
                func=sns.barplot, 
                data=data, 
                title='تجربة', 
                x='Confirmed', 
                y='Country/Region'
            ),
            wg.table_plot(
                func=sns.barplot, 
                data=data, 
                title='تجربة', 
                x='Confirmed', 
                y='Country/Region'
            ),
            wg.table_plot(
                func=sns.barplot, 
                data=data, 
                title='تجربة', 
                x='Confirmed', 
                y='Country/Region'
            ),
        ),
        (
            wg.table_plot(
                func=sns.barplot, 
                data=data, 
                title='تجربة', 
                x='Confirmed', 
                y='Country/Region'
            ),
            wg.table_plot(
                func=sns.barplot, 
                data=data, 
                title='تجربة', 
                x='Confirmed', 
                y='Country/Region'
            ),
            wg.table_plot(
                func=sns.barplot, 
                data=data, 
                title='تجربة', 
                x='Confirmed', 
                y='Country/Region'
            ),
            wg.table_plot(
                func=sns.barplot, 
                data=data, 
                title='تجربة', 
                x='Confirmed', 
                y='Country/Region'
            ),
        ),
    ), alignment=CENTER)

    return widget