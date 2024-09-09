# -*- coding: utf-8 -*-
"""
A script to demonstrate how to fetch public power production data from the energy-charts API and transform it to a dataframe.
"""

from src.api_accessor import EnergyChartsAPI
from src.api_response_processor import make_public_power_df

if __name__ == "__main__":
    country = "de"
    year = 2024

    api = EnergyChartsAPI()

    public_power = api.get_public_power(
        country=country, start=f"{year}-01-01", end=f"{year}-12-31"
    )

    power_df = make_public_power_df(
        public_power_api_response=public_power,
        power_column_name_dict=api.power_column_dict,
    )

    print(power_df.head())
