from PySide6 import QtWidgets as qw
import seaborn as sns

from utils import *
import widgets as wg
from df import *


def tab_1():
    
    widget = wg.row(
        
        wg.col(

            wg.card(
                "Top 10 Confirmed Cases",
                wg.plot(
                    func=sns.barplot,
                    data=top_confirmed,
                    x="Confirmed",
                    y="Country/Region",
                    palette="crest",
                    size=(420, 290),
                    legend=False,
                ),
                "Countries with highest total infection counts",
            ),

            wg.card(
                "Regional Distribution (WHO)",
                wg.plot(
                    func=sns.barplot,
                    data=region_data,
                    x="Confirmed",
                    y="WHO Region",
                    palette="viridis",
                    size=(420, 290),
                    legend=False,
                ),
                "Total confirmed cases grouped by geographic region",
            ),

            alignment=TOP,
            spacing=16,
            margin=Margin(all=6),
            size_policy=(Size.Expanding, Size.Expanding),
        ),
        wg.col(

            wg.card(
                "Top 10 Mortality Figures",
                wg.plot(
                    func=sns.barplot,
                    data=top_deaths,
                    x="Deaths",
                    y="Country/Region",
                    palette="flare",
                    size=(420, 290),
                    legend=False,
                ),
                "Countries with highest total recorded deaths",
            ),

            wg.card(
                "Top 10 Summary Table",
                wg.table(
                    df[["Country/Region", "Confirmed", "Deaths", "Recovered"]]
                        .sort_values("Confirmed", ascending=False)
                        .head(10),
                    size=(420, 290),
                ),
                "Direct breakdown of country figures",
            ),

            alignment=TOP,
            spacing=16,
            margin=Margin(all=6),
            size_policy=(Size.Expanding, Size.Expanding),
        ),

        alignment=TOP,
        spacing=16,
        margin=Margin(all=12),
        scrollable=True,
        scroll_bar_style=Style(
            background_color=Color.TOW,
            width='10px',
            margin='0px',
            border_radius='5px',
        ),
        scroll_bar_handle_style=Style(
            background_color=Color.THREE,
            min_height='20px',
            border_radius='5px',
        ),
        scroll_bar_handle_hover_style=Style(
            background_color=Color.EIGHT,
        ),
    )

    return widget
