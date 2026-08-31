from PySide6 import QtWidgets as qw
import seaborn as sns
import matplotlib.pyplot as plt

from utils import *
import widgets as wg
from df import df


def create_card_container(title: str, widget_content: qw.QWidget, subtitle: str = None) -> qw.QFrame:
    """Wraps any chart or table inside a structured modern card frame with header."""
    card = qw.QFrame()
    card.setStyleSheet("""
        QFrame {
            background-color: #FFFFFF;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
        }
    """)
    
    header_layout = qw.QVBoxLayout()
    header_layout.setContentsMargins(16, 14, 16, 6)
    header_layout.setSpacing(2)

    title_label = qw.QLabel(title)
    title_label.setStyleSheet("font-size: 15px; font-weight: 700; color: #00465C; border: none;")
    header_layout.addWidget(title_label)

    if subtitle:
        sub_label = qw.QLabel(subtitle)
        sub_label.setStyleSheet("font-size: 11px; color: #64748B; border: none;")
        header_layout.addWidget(sub_label)

    content_layout = qw.QVBoxLayout()
    content_layout.setContentsMargins(12, 6, 12, 12)
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
    
    # 3. Regional Aggregation by WHO Region (if available) or Recovery Rate
    if 'WHO Region' in df.columns:
        region_data = df.groupby('WHO Region', as_index=False)[['Confirmed', 'Deaths', 'Recovered']].sum()
    else:
        region_data = df.sort_values('Recovered', ascending=False).head(10)

    # 4. Top Recovery Rates Data
    top_recovery_rate = df.sort_values('Recovered', ascending=False).head(10)

    # Chart 1: Top Confirmed Cases
    chart_confirmed = wg.plot(
        func=sns.barplot,
        data=top_confirmed,
        x='Confirmed',
        y='Country/Region',
        palette="crest",
        size=(500, 320)
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
        size=(500, 320)
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
            size=(500, 320)
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
            size=(500, 320)
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
        size=(500, 320)
    )
    card_table = create_card_container(
        "Top 10 Summary Table", 
        table_summary, 
        "Direct breakdown of country figures"
    )

    left_column = wg.col(
        card_confirmed,
        card_region,
        alignment=TOP,
        spacing=18,
        margin=Margin(all=8)
    )

    right_column = wg.col(
        card_deaths,
        card_table,
        alignment=TOP,
        spacing=18,
        margin=Margin(all=8)
    )

    # Main scrollable dashboard layout
    dashboard_layout = wg.row(
        left_column,
        right_column,
        alignment=TOP,
        spacing=18,
        margin=Margin(all=12),
        scrollable=True
    )

    return dashboard_layout