# -*- coding: utf-8 -*-
"""A script to demonstrate how to fetch data from the energy-charts API."""

from datetime import datetime

import pandas as pd

from functions import (
    get_power,
    get_installed_power,
    get_price_spot_market
    )


COUNTRIES = [
    'ch',  # Switzerland
    'eu',  # European
    'all',  # Europe Union
    'al',  # Albania
    'am',  # Armenia
    'at',  # Austria
    'az',  # Azerbaijan
    'ba',  # Bosnia-Herzegovina
    'be',  # Belgium
    'by',  # Belarus
    'cy',  # Cyprus
    'cz',  # Czech Republic
    'de',  # Germany
    'dk',  # Denmark
    'ee',  # Estonia
    'es',  # Spain
    'fi',  # Finland
    'fr',  # France
    'ge',  # Georgia
    'gr',  # Greece
    'hr',  # Croatia
    'hu',  # Hungary
    'ie',  # Ireland
    'lt',  # Lithuania
    'lu',  # Luxembourg
    'lv',  # Latvia
    'md',  # Moldova
    'me',  # Montenegro
    'mk',  # North Macedonia
    'mt',  # Malta
    'nie',  # North Ireland
    'nl',  # Netherlands
    'no',  # Norway
    'pl',  # Poland
    'pt',  # Portugal
    'ro',  # Romania
    'rs',  # Serbia
    'ru',  # Russia
    'se',  # Sweden
    'sl',  # Slovenia
    'sk',  # Slovak Republic
    'tr',  # Turkey
    'ua',  # Ukraine
    'uk',  # United Kingdom
    'xk',  # Kosovo
    ]

YEARS = [year for year in range(2015, 2023)]

if __name__ == '__main__':
    # Usage example for the get_power() function.
    # power = get_power(
    #     country='lu', start='2022-01-01T00:00Z', end='2023-01-01T00:00Z'
    #     )

    # Usage example for the get_installed_power() function.
    # installed_power = get_installed_power(
    #     country='de', time_step='yearly', installation_decomission=False
    #     )

    # Usage example for the get_price_spot_market() function.
    price_spot_market = get_price_spot_market(
        bzn='DE-LU', start='2022-01-01T00:00Z', end='2022-01-02T00:00Z'
        )

    # %%

    # for country in COUNTRIES:
    #     for year in YEARS:
    #         try:
    #             power = get_power(
    #                 country=country, start=f'{year}-01-01T00:00Z', end=f'{year+1}-01-01T00:00Z'
    #                 )
    #             power_df = pd.DataFrame(power)
    #             a = power_df['xAxisValues (Unix timestamp)']
    #             timestamp = [datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S') for dt in power_df['xAxisValues (Unix timestamp)']]
    #             power_df.index = timestamp
    #             power_df.index.name = 'timestamp_utc'
    #             del power_df['xAxisValues (Unix timestamp)']
                
    #             power_df.to_csv(f'C:/Users/s13c2d/Desktop/Lastprofile_Laender/installed_power_{country}_{year}.csv',
    #                             index=True, sep=';', decimal='.')
    #         except:
    #             print(f'data for {country} in {year} not found')

    # for country in COUNTRIES:
    #     try:
    #         installed_power = get_installed_power(
    #             country=country, time_step='yearly', installation_decomission=True
    #             )
    #         installed_power_df = pd.DataFrame(installed_power)
    #         installed_power_df.set_index('years', inplace=True)
    #         installed_power_df.index.name = 'year'
    #         installed_power_df.to_csv(f'C:/Users/s13c2d/Desktop/Stilllegung_Laender/installation_decomission_{country}.csv',
    #                                   index=True, sep=';', decimal='.')
    #     except:
    #         print(f'data for {country} not found')
