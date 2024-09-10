# -*- coding: utf-8 -*-
"""
A script to demonstrate how to fetch installed power data from the energy-charts API and transform it to a dataframe.
"""

from src.api_accessor import EnergyChartsAPI
from src.api_response_processor import make_installed_power_df

if __name__ == "__main__":
    time_step = "yearly"
    country = "uk"
    plot = True

    api = EnergyChartsAPI()
    installed_power = api.get_installed_power(
        country=country, time_step=time_step, installation_decomission=True
    )

    installed_power_df = make_installed_power_df(
        installed_power_api_response=installed_power, time_step=time_step
    )

    if plot:
        import plotly.io as pio
        import plotly_express as px

        pio.renderers.default = "browser"

        installed_power_df.set_index("year", inplace=True)
        fig = px.line(
            installed_power_df, x=installed_power_df.index, y=installed_power_df.columns
        )
        fig.show()
