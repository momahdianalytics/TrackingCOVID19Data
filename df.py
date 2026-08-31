import pandas as pd


df = pd.read_csv('data/country_wise_latest.csv')

# 1. Top 10 Confirmed Cases Data
top_confirmed = df.sort_values(
    "Confirmed",
    ascending=False,
).head(10)

# 2. Top 10 Deaths Data
top_deaths = df.sort_values(
    "Deaths",
    ascending=False,
).head(10)

# 3. Regional Aggregation by WHO Region
region_data = (
    df.groupby("WHO Region", as_index=False)[
        ["Confirmed", "Deaths", "Recovered"]
    ]
    .sum()
    .sort_values(
        "Confirmed",
        ascending=False,
    )
)



# 4. Top 10 Recovered Cases Data
top_recovered = df.sort_values(
    "Recovered",
    ascending=False,
).head(10)

# 5. Top 10 Active Cases Data
top_active = df.sort_values(
    "Active",
    ascending=False,
).head(10)

