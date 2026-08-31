from PySide6 import QtWidgets as qw
import seaborn as sns

from utils import *
import widgets as wg
from df import *


def tab_2():
    
    widget = wg.row(
        
        wg.col(

            wg.card(
                "Recovered vs Deaths (WHO Region)",
                wg.plot(
                    func=sns.scatterplot,
                    data=df,
                    x="Recovered",
                    y="Deaths",
                    hue="WHO Region",
                    palette="crest",
                    size=(420, 290),
                ),
                "Recovered vs Deaths grouped by geographic region",
            ),

            wg.card(
                "Confirmed vs Active (WHO Region)",
                wg.plot(
                    func=sns.scatterplot,
                    data=df,
                    x="Active",
                    y="Confirmed",
                    hue="WHO Region",
                    palette="crest",
                    size=(420, 290),
                ),
                "Confirmed vs Active grouped by geographic region",
            ),

            alignment=TOP,
            spacing=16,
            margin=Margin(all=6),
            size_policy=(Size.Expanding, Size.Expanding),
        ),
        wg.col(

            wg.card(
                "Top 10 Active Cases",
                wg.plot(
                    func=sns.barplot,
                    data=top_active,
                    x="Active",
                    y="Country/Region",
                    palette="flare",
                    size=(420, 290),
                    legend=False,
                ),
                "Countries with highest total recorded active cases",
            ),

            wg.card(
                "Top 10 Active Cases Summary Table",
                wg.table(
                    df[["Country/Region", "Confirmed", "Active", "Recovered"]]
                        .sort_values("Active", ascending=False)
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
    )

    return widget
