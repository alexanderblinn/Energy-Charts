# -*- coding: utf-8 -*-
"""
A script to demonstrate how to fetch installed power data from the energy-charts API.
"""

from src.api_accessor import EnergyChartsAPI

if __name__ == "__main__":
    country = "de"

    api = EnergyChartsAPI()
    installed_power = api.get_installed_power(
        country=country, time_step="yearly", installation_decomission=True
    )
