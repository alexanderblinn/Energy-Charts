# -*- coding: utf-8 -*-
"""A script to demonstrate how to fetch data from the energy-charts API."""


from functions import (
    get_power,
    get_installed_power,
    get_price_spot_market
    )


if __name__ == '__main__':
    # Usage example for the get_power() function.
    power = get_power(
        country='de', start='2022-01-01T17:00Z', end='2022-01-02T17:00Z'
        )

    # Usage example for the get_installed_power() function.
    installed_power = get_installed_power(
        country='de', time_step='monthly', installation_decomission=False
        )

    # Usage example for the get_price_spot_market() function.
    price_spot_market = get_price_spot_market(
        bzn='DE-LU', start='2022-01-01T17:00Z', end='2022-01-02T17:00Z'
        )
