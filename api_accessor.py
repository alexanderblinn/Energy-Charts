# -*- coding: utf-8 -*-
"""A simple class for accessing the API of the energy-charts website."""


from enum import Enum
import requests
from typing import Any


class ValidationError(TypeError):
    """Custom Validation Error."""


class DataType(Enum):
    """An enumeration of data types for the energy-charts API."""

    POWER = 'power'
    INSTALLED_POWER = 'installed_power'
    PRICE_SPOT_MARKET = 'price_spot_market'


class EnergyChartsAPI:
    """A class for interacting with the energy-charts API."""

    def __init__(self):
        """Initialize the API client."""
        self.base_url: str = 'https://api.energy-charts.info'

    @staticmethod
    def _join_string(symbol: str, first_string: str, second_string: str
                     ) -> str:
        return symbol.join([first_string, second_string])

    def download_data(self, data_type: DataType, parameters: dict
                      ) -> dict[Any]:
        """
        Download data from the energy-charts API.

        Parameters
        ----------
        data_type : str
            The type of data to fetch.
        parameters : dict
            A dictionary of parameters to pass to the API.

        Raises
        ------
        ValueError
            A ValueError is raised if the response code is not 200.

        Returns
        -------
        dict[Any]
            A dictionary containing the API response data.

        """
        url = self._join_string('/', self.base_url, data_type)
        response = requests.get(url, params=parameters)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValidationError(f'An error occurred: {response.text}')
