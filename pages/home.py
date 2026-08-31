from PySide6 import QtWidgets as qw
import seaborn as sns

from utils import *
import widgets as wg
from df import df


def create_card_container(title: str, widget_content: qw.QWidget, subtitle: str = None) -> qw.QFrame:
    """Wraps any chart or table inside a structured modern card frame with expanding layout."""
    card = qw.QFrame()
    card.setStyleSheet("""
        QFrame {
            background-color: #1E293B;
            border-radius: 12px;
            border: 1px solid #334155;
        }
    """)
    card.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)
    
    header_layout = qw.QVBoxLayout()
    header_layout.setContentsMargins(18, 14, 18, 4)
    header_layout.setSpacing(2)

    title_label = qw.QLabel(title)
    title_label.setStyleSheet("font-size: 15px; font-weight: 700; color: #38BDF8; border: none; background: transparent;")
    header_layout.addWidget(title_label)

    if subtitle:
        sub_label = qw.QLabel(subtitle)
        sub_label.setStyleSheet("font-size: 11px; color: #94A3B8; border: none; background: transparent;")
        header_layout.addWidget(sub_label)

    content_layout = qw.QVBoxLayout()
    content_layout.setContentsMargins(12, 4, 12, 12)
    content_layout.addWidget(widget_content)

    main_layout = qw.QVBoxLayout(card)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)
    main_layout.addLayout(header_layout)
    main_layout.addLayout(content_layout)

    return card


def home():
    # 1. Top 10 Confirmed Cases Data
    top_confirmed = df.sort_values('Confirmed', ascending=False).head(10)
    
    # 2. Top 10 Deaths Data
    top_deaths = df.sort_values('Deaths', ascending=False).head(10)
    
    # 3. Regional Aggregation by WHO Region
    if 'WHO Region' in df.columns:
        region_data = df.groupby('WHO Region', as_index=False)[['Confirmed', 'Deaths', 'Recovered']].sum()
        region_data = region_data.sort_values('Confirmed', ascending=False)
    else:
        region_data = df.sort_values('Recovered', ascending=False).head(10)

    # Chart 1: Top Confirmed Cases
    chart_confirmed = wg.plot(
        func=sns.barplot,
        data=top_confirmed,
        x='Confirmed',
        y='Country/Region',
        palette="crest",
        size=(420, 290)
    )
    card_confirmed = create_card_container(
        "Top 10 Confirmed Cases", 
        chart_confirmed, 
        "Countries with highest total infection counts"
    )

    # Chart 2: Top Deaths
    chart_deaths = wg.plot(
        func=sns.barplot,
        data=top_deaths,
        x='Deaths',
        y='Country/Region',
        palette="flare",
        size=(420, 290)
    )
    card_deaths = create_card_container(
        "Top 10 Mortality Figures", 
        chart_deaths, 
        "Countries with highest total recorded deaths"
    )

    # Chart 3: Regional Distribution (WHO Regions)
    if 'WHO Region' in df.columns:
        chart_region = wg.plot(
            func=sns.barplot,
            data=region_data,
            x='Confirmed',
            y='WHO Region',
            palette="viridis",
            size=(420, 290)
        )
        card_region = create_card_container(
            "Regional Distribution (WHO)", 
            chart_region, 
            "Total confirmed cases grouped by geographic region"
        )
    else:
        chart_region = wg.plot(
            func=sns.barplot,
            data=region_data,
            x='Recovered',
            y='Country/Region',
            palette="mako",
            size=(420, 290)
        )
        card_region = create_card_container(
            "Top Recoveries", 
            chart_region, 
            "Highest recovery figures recorded"
        )

    # Chart 4: Table View of Top Data
    summary_cols = ['Country/Region', 'Confirmed', 'Deaths', 'Recovered']
    available_cols = [c for c in summary_cols if c in df.columns]
    table_summary = wg.table(
        df[available_cols].sort_values('Confirmed', ascending=False).head(10),
        size=(420, 290)
    )
    card_table = create_card_container(
        "Top 10 Summary Table", 
        table_summary, 
        "Direct breakdown of country figures"
    )

    # Left and Right responsive columns
    left_column = wg.col(
        card_confirmed,
        card_region,
        alignment=TOP,
        spacing=16,
        margin=Margin(all=6)
    )
    left_column.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)

    right_column = wg.col(
        card_deaths,
        card_table,
        alignment=TOP,
        spacing=16,
        margin=Margin(all=6)
    )
    right_column.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)

    # Main dashboard grid
    dashboard_layout = wg.row(
        left_column,
        right_column,
        alignment=TOP,
        spacing=16,
        margin=Margin(all=12),
        scrollable=True
    )

    return dashboard_layout