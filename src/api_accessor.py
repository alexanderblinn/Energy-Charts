# -*- coding: utf-8 -*-
"""A simple class for accessing the API of the energy-charts website."""

import requests


class EnergyChartsAPI:
    """A class for interacting with the energy-charts API."""

    base_url = "https://api.energy-charts.info"

    def __init__(self):
        pass

    def get_installed_power(
        self, country: str, time_step: str, installation_decomission: bool
    ) -> dict[list[float | None]]:
        """
        Get installed power capacity data for a given country and time step.

        Parameters
        ----------
        country : str
            The code for the country for which data is to be fetched.
        time_step : str
            The time step for the data. Can be 'yearly', or 'monthly'.
            'monthly' is only available for Germany.
        installation_decomission : bool
            If true, the installation / decomission numbers are returned.

        Returns
        -------
        dict[list[float | None]]
            A dictionary containing the API response data.
        """
        if time_step not in ["yearly", "monthly"]:
            raise ValueError('The time step must be either "yearly" or "monthly".')
        country = country.lower()
        url = f"{self.base_url}/installed_power?country={country}&time_step={time_step}&installation_decomission={installation_decomission}"
        response = requests.get(url)
        return response.json()

    def get_power_production(
        self, country: str, start: str, end: str, power_type: str
    ) -> dict[list[float | None]]:
        """
        Get electricity production by type for a given country and period.
        :param country:
        :param start:
        :param end:
        :param power_type: 'public' or 'total' ('total' includes industrial self-supply)
        :return:
        """
        if power_type not in ["public", "total"]:
            raise ValueError('The power type must be either "public" or "total".')
        country = country.lower()
        url = f"{self.base_url}/{power_type}_power?country={country}&start={start}&end={end}"
        response = requests.get(url)
        return response.json()
