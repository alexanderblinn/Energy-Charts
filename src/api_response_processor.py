# -*- coding: utf-8 -*-
"""Functions to process energy-charts API responses for plotting and further analyses."""
from datetime import datetime

import pandas as pd

from src.globals import POWER_COLUMN_NAME_DICT


def make_power_df(power_api_response) -> pd.DataFrame:
    """
    Create a pandas DataFrame from the API response for public or total power data.

    :param power_api_response: return of api call to get_public_power
    :return: power_df (pandas DataFrame) with columns timestamp_utc, and one column per power type
    """

    timestamp = power_api_response["unix_seconds"]
    timestamp = [
        datetime.utcfromtimestamp(dt).strftime("%Y-%m-%d %H:%M:%S") for dt in timestamp
    ]
    power_df = pd.DataFrame({"timestamp_utc": timestamp})
    power_df = _add_production_type_columns(
        power_df=power_df, production_types_list=power_api_response["production_types"]
    )

    return power_df


def make_installed_power_df(
    installed_power_api_response: dict[list[float | None]], time_step: str = "yearly"
) -> pd.DataFrame:
    """
    Create a pandas DataFrame from the API response for installed power data.

    :param installed_power_api_response: return of api call to get_installed_power
    :param time_step: the time step for the data. Can be 'yearly', or 'monthly'.
    :return: installed_power_df (pandas DataFrame) with columns year, and one column per power type
    """

    timestamp = installed_power_api_response["time"]
    if time_step == "monthly":
        timestamp = [datetime.strptime(dt, "%m.%Y") for dt in timestamp]
        time_col_name = "month"

    if time_step == "yearly":
        time_col_name = "year"
        timestamp = [int(dt) for dt in timestamp]

    power_df = pd.DataFrame({time_col_name: timestamp})
    power_df = _add_production_type_columns(
        power_df=power_df,
        production_types_list=installed_power_api_response["production_types"],
    )
    return power_df


def _add_production_type_columns(
    power_df: pd.DataFrame, production_types_list: list[dict]
) -> pd.DataFrame:
    for i in range(len(production_types_list)):
        _name = production_types_list[i]["name"]
        _col_name = POWER_COLUMN_NAME_DICT[_name]
        power_df[_col_name] = production_types_list[i]["data"]
    return power_df
