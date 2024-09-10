# -*- coding: utf-8 -*-
"""
A script to demonstrate how to fetch data from the energy-charts API.
Loops over all years and countries to fetch data and save it to a CSV file.
Aggregates data to daily resolution.
Smoothes daily data using a centered moving average.
Creates plotly line plot html file for each country showing the 10year trend of energy production by energy source.
"""

import os

import pandas as pd
import plotly_express as px

from src.api_accessor import EnergyChartsAPI
from src.api_response_processor import make_power_df
from src.globals import COUNTRY_NAME_DICT, POWER_COLUMN_NAME_DICT

power_type = "public"
window_size_ma = 50
years = [year for year in range(2015, 2025)]
countries = COUNTRY_NAME_DICT

if __name__ == "__main__":
    local_data_dir = os.path.join("..", "data")
    local_plot_dir = os.path.join("..", "plots")

    if not os.path.exists(local_data_dir):
        os.makedirs(local_data_dir)

    if not os.path.exists(local_plot_dir):
        os.makedirs(local_plot_dir)

    api = EnergyChartsAPI()
    for country in countries:
        csv_file_name_daily = os.path.join(
            local_data_dir, f"{country}_{power_type}_power_daily.csv"
        )
        if os.path.exists(csv_file_name_daily):
            power_df_daily = pd.read_csv(csv_file_name_daily, index_col=0)
            power_df_daily.index = pd.to_datetime(power_df_daily.index)
            col_names = [
                c for c in POWER_COLUMN_NAME_DICT if c in power_df_daily.columns
            ]
        else:
            power_df_list = []
            for year in years:
                csv_file_name = os.path.join(
                    local_data_dir, f"{country}_{power_type}_power_{year}.csv"
                )
                if os.path.exists(csv_file_name):
                    power_df = pd.read_csv(csv_file_name)
                else:
                    try:
                        api_response = api.get_power_production(
                            country=country,
                            start=f"{year}-01-01",
                            end=f"{year}-12-31",
                            power_type=power_type,
                        )
                    except Exception as e:
                        print(
                            f"Failed to fetch {power_type} production data for {country}-{year}. Error: {e}"
                        )
                        continue
                    power_df = make_power_df(power_api_response=api_response)
                    power_df.to_csv(csv_file_name)
                    del csv_file_name, api_response

                print(f"Data processed for {country}-{year}.")
                power_df_list.append(power_df)

            if len(power_df_list) == 0:
                continue
            power_df = pd.concat(power_df_list)
            power_df["date"] = pd.to_datetime(power_df["timestamp_utc"]).dt.date
            col_names = [
                c for c in POWER_COLUMN_NAME_DICT.values() if c in power_df.columns
            ]
            power_df_daily = power_df.groupby("date")[col_names].mean()
            power_df_daily.to_csv(csv_file_name_daily)
            del csv_file_name_daily, power_df_list, power_df

        for col in col_names:
            power_df_daily[f"{col}_{window_size_ma}ma"] = (
                power_df_daily[col].rolling(window=window_size_ma, center=True).mean()
            )

        y_cols = [f"{col}_{window_size_ma}ma" for col in col_names]
        default_show_cols = [
            f"nuclear_{window_size_ma}ma",
            f"fossil_brown_coal_{window_size_ma}ma",
            f"fossil_hard_coal_{window_size_ma}ma",
            f"fossil_oil_{window_size_ma}ma",
            f"fossil_coal_gas_{window_size_ma}ma",
            f"fossil_gas_{window_size_ma}ma",
        ]
        _fig = px.line(
            power_df_daily,
            x=power_df_daily.index,
            y=y_cols,
            title=f"{COUNTRY_NAME_DICT[country]}: {window_size_ma} Day Centered Moving Averages of {power_type} Energy Production'. Source: https://api.energy-charts.info/",
        )
        for trace in _fig.data:
            if trace.name in default_show_cols:
                trace.visible = True
            else:
                trace.visible = "legendonly"

        _fig.update_layout(legend_title_text="Generator/Load Type")
        _fig.update_layout(yaxis_title="Energy Production (MW)")
        _fig.write_html(
            os.path.join(
                local_plot_dir, f"{country}_{power_type}_energy_mix_daily_smoothed.html"
            )
        )
