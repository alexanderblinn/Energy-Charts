# -*- coding: utf-8 -*-
"""Some helper functions for the EnergyChartsAPI class."""

from typing import Any

from api_accessor import EnergyChartsAPI


def _get(data_type: str, *args) -> dict[Any]:
    api = EnergyChartsAPI()
    return api.download_data(data_type, *args)


def get_power(country: str, start: str, end: str) -> dict[list[float | None]]:
    """
    Get public electricity production by type for a given country and period.

    Parameters
    ----------
    country : str
        The code for the country for which data is to be fetched.
    start : str
        The start timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.
    end : str
        The end timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.

    Returns
    -------
    dict[list[float]]
        A dictionary containing the API response data.
    """
    parameters = {
        'country': country,
        'start': start,
        'end': end
    }
    return _get('power', parameters)


def get_installed_power(country: str, time_step: str,
                        installation_decomission: bool
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
    parameters = {
        'country': country,
        'time_step': time_step,
        'installation_decomission': str(installation_decomission).lower()
    }
    return _get('installed_power', parameters)


def get_price_spot_market(bzn: str, start: str, end: str
                          ) -> dict[list[float | None]]:
    """
    Get spot market price data for a given bidding zone and time period.

    Parameters
    ----------
    bzn : str
        The bidding zone (bzn) code for which data is to be fetched.
    start : str
        The start timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.
    end : str
        The end timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.

    Returns
    -------
    dict[list[float | None]]
        A dictionary containing the API response data.
    """
    parameters = {
        'bzn': bzn,
        'start': start,
        'end': end
        }
    return _get('price_spot_market', parameters)
