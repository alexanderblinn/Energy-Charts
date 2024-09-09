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
    for i in range(len(public_power_api_response["production_types"])):
        _name = public_power_api_response["production_types"][i]["name"]
        _col_name = power_column_name_dict[_name]
        power_df[_col_name] = public_power_api_response["production_types"][i]["data"]

    return power_df
