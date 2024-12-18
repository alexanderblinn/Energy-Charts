# -*- coding: utf-8 -*-
"""
This module provides a client for accessing the Energy Charts API.

Classes:
    _BaseEnergyChartsAPI: A base class for making API requests to the Energy Charts API.
    EnergyChartsAPI: A derived class that provides specific methods for accessing various endpoints of the Energy Charts API.
"""

from typing import Any

import requests

from app.enums import (
    BindingZones,
    Countries,
    Endpoints,
    ForecastType,
    ProductionType,
    Regions,
    SubTypes,
    TimeSteps,
)


class ValidationError(Exception):
    """Raised for validation errors when the API returns a 422 status code."""


class APIRequestError(Exception):
    """Raised for unexpected API errors or non-200/422 status codes."""


class _BaseEnergyChartsAPI:
    BASE_URL = "https://api.energy-charts.info"

    def __init__(self):
        self.session = requests.Session()

    def get(
        self, endpoint: Endpoints, **kwargs: dict[str, str | bool | int]
    ) -> dict[str, Any] | None:
        url = f"{self.BASE_URL}/{endpoint.value}"
        params = {k: v for k, v in kwargs.items() if v is not None}  # Skip None values
        response = self.session.get(url, params=params)
        match response.status_code:
            case 200:
                return response.json()
            case 422:
                raise ValidationError(response.json())
            case _:
                raise APIRequestError(f"Unexpected status code: {response.status_code}")


class EnergyChartsAPI(_BaseEnergyChartsAPI):
    """A class for interacting with the Energy Charts API."""

    def get_public_power(
        self, country: Countries, start: str, end: str, subtype: SubTypes | None = None
    ) -> dict | None:
        """Returns the public net electricity production for a given country for each production type.

        Parameters:
            country (Countries): The target country.
            start (str): Start date of the data range in ISO 8601, daily format, or UNIX timestamp.
                         Examples: '2024-01-01T17:00Z', '2024-01-01T18:00+01:00' '2024-01-01', '1704063600'.
            end (str): End date of the data range in the same formats as start.
            subtype (SubTypes | None): Optional subtype.

        Returns:
            dict | None: Response schema:
                {
                    "unix_seconds": [int],
                    "forecast_values": [float],
                    "production_type": str,
                    "forecast_type": str,
                    "deprecated": bool
                }
        """
        return self.get(
            Endpoints.PUBLIC_POWER,
            country=country.value,
            start=start,
            end=end,
            subtype=subtype.value if subtype is not None else None,
        )

    def get_public_power_forecast(
        self,
        country: Countries,
        production_type: ProductionType,
        forecast_type: ForecastType,
        start: str,
        end: str,
    ) -> dict | None:
        """Returns the forecast of the public net electricity production for a given country for each production type.

        Parameters:
            country (Countries): The target country.
            production_type (ProductionType): The production type.
            forecast_type (ForecastType): The forecast type.
            start (str): Start date of the data range in ISO 8601, daily format, or UNIX timestamp.
                         Examples: '2024-01-01T17:00Z', '2024-01-01T18:00+01:00' '2024-01-01', '1704063600'.
            end (str): End date of the data range in the same formats as start.

        Returns:
            dict | None: Response schema:
                {
                    "unix_seconds": list[int],
                    "forecast_values": list[float],
                    "production_type": str,
                    "forecast_type": str,
                    "deprecated": bool
                }
        """
        return self.get(
            Endpoints.PUBLIC_POWER_FORECAST,
            country=country.value,
            production_type=production_type.value,
            forecast_type=forecast_type.value,
            start=start,
            end=end,
        )

    def get_total_power(self, country: Countries, start: str, end: str) -> dict | None:
        """Returns the total net electricity production (including industrial self supply) for a given country for each production type.

        Parameters:
            country (Countries): The target country.
            start (str): Start date of the data range in ISO 8601, daily format, or UNIX timestamp.
                         Examples: '2024-01-01T17:00Z', '2024-01-01T18:00+01:00' '2024-01-01', '1704063600'.
            end (str): End date of the data range in the same formats as start.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": list[int],
                "production_types": [
                {
                    "name": str,
                    "data": list[float]
                }
                ],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.TOTAL_POWER, country=country.value, start=start, end=end)

    def get_installed_power(
        self, country: Countries, time_step: TimeSteps, installation_decommission: bool
    ) -> dict | None:
        """Returns the installed power for a specified country in GW except for battery storage capacity, which is given in GWh.

        Parameters:
            country (Countries): The target country.
            time_step (TimeSteps): The time step for the data.
            installation_decommission (bool): If true, the net installation / decommission numbers are returned instead of total installed power.

        Returns:
            dict | None: Response schema:
            {
                "time": list[str],
                "production_types": [
                {
                    "name": str,
                    "data": list[float]
                }
                ],
                "deprecated": bool
            }
        """
        return self.get(
            Endpoints.INSTALLED_POWER,
            country=country.value,
            time_step=time_step.value,
            installation_decommission=installation_decommission,
        )

    def get_frequency(self, region: Regions, start: str, end: str) -> dict | None:
        """Returns the frequency measured at Fraunhofer ISE in Freiburg, Germany.

        Parameters:
            region (Regions): The target region.
            start (str): Start date of the data range in ISO 8601, daily format, or UNIX timestamp.
                         Examples: '2024-01-01T17:00Z', '2024-01-01T18:00+01:00' '2024-01-01', '1704063600'.
            end (str): End date of the data range in the same formats as start.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": list[int],
                "data": list[float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.FREQUENCY, region=region.value, start=start, end=end)

    def get_cbet(self, country: Countries, start: str, end: str) -> dict | None:
        """
        Returns the cross-border electricity trading (cbet) in GW between a specified country and its neighbors.
        Positive values indicate an import of electricity, whereas negative values show electricity exports.

        Parameters:
            country (Countries): The target country.
            start (str): Start date of the data range in ISO 8601, daily format, or UNIX timestamp.
                            Examples: '2024-01-01T17:00Z', '2024-01-01T18:00+01:00' '2024-01-01', '1704063600'.
            end (str): End date of the data range in the same formats as start.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": [int],
                "countries": [
                    {
                    "name": str,
                    "data": [float]
                    }
                ],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.CBET, country=country.value, start=start, end=end)

    def get_cbpf(self, country: Countries, start: str, end: str) -> dict | None:
        """
        Returns the cross-border physical flows (cbpfs) of electricity in GW between a specified country and its neighbors.
        Positive values indicate an import of electricity, whereas negative values show electricity exports.

        Parameters:
            country (Countries): The target country.
            start (str): Start date of the data range in ISO 8601, daily format, or UNIX timestamp.
                            Examples: '2024-01-01T17:00Z', '2024-01-01T18:00+01:00' '2024-01-01', '1704063600'.
            end (str): End date of the data range in the same formats as start.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": [int],
                "countries": [
                    {
                    "name": str,
                    "data": [float]
                    }
                ],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.CBPF, country=country.value, start=start, end=end)

    def get_price(self, bzn: BindingZones, start, end) -> dict | None:
        """Returns the day-ahead spot market price for a specified bidding zone in EUR/MWh.

        Parameters:
            bzn (BindingZones): The target bidding zone.
            start (str): Start date of the data range in ISO 8601, daily format, or UNIX timestamp.
                            Examples: '2024-01-01T17:00Z', '2024-01-01T18:00+01:00' '2024-01-01', '1704063600'.
            end (str): End date of the data range in the same formats as start.

        Returns:
            dict | None: Response schema:
            {
                "license_info": str,
                "unix_seconds": [int],
                "price": [float],
                "unit": str,
                "deprecated": bool
            }
        """
        return self.get(Endpoints.PRICE, bzn=bzn.value, start=start, end=end)

    def get_signal(self, country: Countries, postal_code: str) -> dict | None:
        """
        Returns the renewable share of load in percent from today until prediction is currently available and the corresponding traffic light.
        If no data is available from the primary data providers, a best guess is made from historic data.
        This is indicated by "substitute" set to True.

        Parameters:
            country (Countries): The target country.
            postal_code (str): The postal code of the target county (indicates local grid state (e.g. transmission line overload)).
                               Note: not available yet

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": [int],
                "share": [float],
                "signal": [int],
                "substitute": bool,
                "deprecated": bool
            }
            Note: The traffic light "signal" is indicated by the following numbers:
                -1: Red (grid congestion)
                0: Red (low renewable share)
                1: Yellow (average renewable share)
                2: Green (high renewable share)
        """
        return self.get(Endpoints.SIGNAL, country=country.value, postal_code=postal_code)

    def get_ren_share_forecast(self, country: Countries) -> dict | None:
        """
        Returns the renewable share of load forecast in percent from today until prediction is currently available. It also includes the forecast for solar, wind on- and offshore share of load.
        If no data is available from the primary data providers, a best guess is made from historic data. This is indicated by "substitute" set to True.

        Parameters:
            country (Countries): The target country.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": [int],
                "ren_share": [float],
                "solar_share": [float],
                "wind_onshore_share": [float],
                "wind_offshore_share": [float],
                "substitute": bool,
                "deprecated": bool
            }
        """
        return self.get(Endpoints.REN_SHARE_FORECAST, country=country.value)

    def get_ren_share_daily_avg(self, country: Countries, year: int) -> dict | None:
        """Returns the average daily renewable share of load for a given year.

        Parameters:
            country (Countries): The target country.
            year (int): The target year. Type -1 for the last year.

        Returns:
            dict | None: Response schema:
            {
                "days": ["dd.mm.yyyy"],
                "data": [float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.REN_SHARE_DAILY_AVG, country=country.value, year=year)

    def get_solar_share(self, country: Countries) -> dict | None:
        """
        Returns the solar share of load from today until prediction is currently available.

        Parameters:
            country (Countries): The target country.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": list[int],
                "data": list[float],
                "forecast": list[float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.SOLAR_SHARE, country=country.value)

    def get_solar_share_daily_avg(self, country: Countries, year: int) -> dict | None:
        """Returns the average daily solar share of load for a given year.

        Parameters:
            country (Countries): The target country.
            year (int): The target year. Type -1 for the last year.

        Returns:
            dict | None: Response schema:
            {
                "days": ["dd.mm.yyyy"],
                "data": [float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.SOLAR_SHARE_DAILY_AVG, country=country.value, year=year)

    def get_wind_onshore_share(self, country: Countries) -> dict | None:
        """Returns the wind onshore share of load from today until prediction is currently available.

        Parameters:
            country (Countries): The target country.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": list[int],
                "data": list[float],
                "forecast": list[float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.WIND_ONSHORE_SHARE, country=country.value)

    def get_wind_onshore_share_daily_avg(self, country: Countries, year: int) -> dict | None:
        """Returns the average daily wind onshore share of load for a given year.

        Parameters:
            country (Countries): The target country.
            year (int): The target year. Type -1 for the last year.

        Returns:
            dict | None: Response schema:
            {
                "days": ["dd.mm.yyyy"],
                "data": [float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.WIND_ONSHORE_SHARE_DAILY_AVG, country=country.value, year=year)

    def get_wind_offshore_share(self, country: Countries) -> dict | None:
        """Returns the wind offshore share of load from today until prediction is currently available.

        Parameters:
            country (Countries): The target country.

        Returns:
            dict | None: Response schema:
            {
                "unix_seconds": list[int],
                "data": list[float],
                "forecast": list[float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.WIND_OFFSHORE_SHARE, country=country.value)

    def get_wind_offshore_share_daily_avg(self, country: Countries, year: int) -> dict | None:
        """Returns the average daily wind offshore share of load for a given year.

        Parameters:
            country (Countries): The target country.
            year (int): The target year. Type -1 for the last year.

        Returns:
            dict | None: Response schema:
            {
                "days": ["dd.mm.yyyy"],
                "data": [float],
                "deprecated": bool
            }
        """
        return self.get(Endpoints.WIND_OFFSHORE_SHARE_DAILY_AVG, country=country.value, year=year)
