# -*- coding: utf-8 -*-
"""A simple class for accessing the API of the energy-charts website."""

import requests


class EnergyChartsAPI:
    """A class for interacting with the energy-charts API."""

    supported_countries = {
        "ch": "Switzerland",
        "eu": "European",
        "all": "Europe Union",
        #       "al": "Albania",
        #       "am": "Armenia",
        "at": "Austria",
        #       "az": "Azerbaijan",
        "ba": "Bosnia-Herzegovina",
        "be": "Belgium",
        #       "by": "Belarus",
        "cy": "Cyprus",
        "cz": "Czech Republic",
        "de": "Germany",
        "dk": "Denmark",
        "ee": "Estonia",
        "es": "Spain",
        "fi": "Finland",
        "fr": "France",
        "ge": "Georgia",
        "gr": "Greece",
        "hr": "Croatia",
        "hu": "Hungary",
        "ie": "Ireland",
        "it": "Italy",
        "lt": "Lithuania",
        "lu": "Luxembourg",
        "lv": "Latvia",
        "md": "Moldova",
        "me": "Montenegro",
        "mk": "North Macedonia",
        #       "mt": "Malta",
        #       "nie": "North Ireland",
        "nl": "Netherlands",
        "no": "Norway",
        "pl": "Poland",
        "pt": "Portugal",
        "ro": "Romania",
        "rs": "Serbia",
        #       "ru": "Russia",
        "se": "Sweden",
        #       "sl": "Slovenia",
        "sk": "Slovak Republic",
        #       "tr": "Turkey",
        "ua": "Ukraine",
        "uk": "United Kingdom",
        "xk": "Kosovo",
    }

    power_column_dict = {
        "Battery Storage (Power)": "battery_storage_power",
        "Battery Storage (Capacity)": "battery_storage_capacity",
        "Hydro pumped storage consumption": "hydro_pumped_storage_cons",
        "Cross border electricity trading": "cross_border_trading",
        "Import Balance": "import_balance",
        "Nuclear": "nuclear",
        "Hydro Run-of-River": "hydro_run_of_river",
        "Biomass": "biomass",
        "Fossil brown coal / lignite": "fossil_brown_coal",
        "Fossil hard coal": "fossil_hard_coal",
        "Fossil oil": "fossil_oil",
        "Fossil coal-derived gas": "fossil_coal_gas",
        "Fossil peat": "fossil_peat",
        "Fossil gas": "fossil_gas",
        "Geothermal": "geothermal",
        "System inertia": "system_inertia",
        "Hydro water reservoir": "hydro_water_reservoir",
        "Hydro pumped storage": "hydro_pumped_storage",
        "Others": "others",
        "Waste": "waste",
        "Wind offshore": "wind_offshore",
        "Wind onshore": "wind_onshore",
        "Solar": "solar",
        "Other renewables": "other_renewables",
        "Other, non-renewable": "other_non_renewable",
        "Marine": "marine",
        "Load": "load",
        "Fossil oil shale": "fossil_oil_shale",
        "Residual load": "residual_load",
        "Renewable share of generation": "renewable_gen_share",
        "Renewable share of load": "renewable_load_share",
    }

    base_url = "https://api.energy-charts.info"

    def __init__(self):
        pass

    def get_public_power(
        self, country: str, start: str, end: str
    ) -> dict[list[float | None]]:
        """
        Get public electricity production by type for a given country and period.
        Public electricity production is the electricity production that is not industrial self-supply.

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
        country = country.lower()
        url = f"{self.base_url}/public_power?country={country}&start={start}&end={end}"
        response = requests.get(url)
        return response.json()

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
