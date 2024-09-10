# -*- coding: utf-8 -*-
"""
A script to demonstrate how to fetch public power production data from the energy-charts API and transform it to a dataframe.
"""

from src.api_accessor import EnergyChartsAPI
from src.api_response_processor import make_power_df

if __name__ == "__main__":
    country = "de"
    power_type = "public"
    year = 2024
    plot = True

    api = EnergyChartsAPI()

    api_response = api.get_power_production(
        country=country,
        start=f"{year}-01-01",
        end=f"{year}-12-31",
        power_type=power_type,
    )

    power_df = make_power_df(power_api_response=api_response)

    if plot:
        import plotly.io as pio
        import plotly_express as px

        pio.renderers.default = "browser"
        power_df.set_index("timestamp_utc", inplace=True)
        fig = px.line(power_df, x=power_df.index, y=power_df.columns)
        fig.show()
