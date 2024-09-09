# -*- coding: utf-8 -*-
"""Functions to process energy-charts API responses for plotting and further analyses."""
from datetime import datetime
import pandas as pd


def make_public_power_df(public_power_api_response, power_column_name_dict):
    """
    Create a pandas DataFrame from the API response for public power data.

    :param public_power_api_response: return of api call to get_public_power
    :param power_column_name_dict: maps api response column names to snake_case column names
    :return: power_df (pandas DataFrame) with columns timestamp_utc, and one column per power type
    """

    timestamp = public_power_api_response["unix_seconds"]
    timestamp = [
        datetime.utcfromtimestamp(dt).strftime("%Y-%m-%d %H:%M:%S") for dt in timestamp
    ]
    power_df = pd.DataFrame({"timestamp_utc": timestamp})
    power_df = _add_production_type_columns(
        power_df=power_df,
        api_response=public_power_api_response,
        power_column_name_dict=power_column_name_dict
    )

    return power_df


def make_installed_power_df(installed_power_api_response, time_step, power_column_name_dict):
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
        api_response=installed_power_api_response,
        power_column_name_dict=power_column_name_dict
    )
    return power_df


def _add_production_type_columns(power_df, api_response, power_column_name_dict):
    for i in range(len(api_response["production_types"])):
        _name = api_response["production_types"][i]["name"]
        _col_name = power_column_name_dict[_name]
        power_df[_col_name] = api_response["production_types"][i]["data"]
    return power_df