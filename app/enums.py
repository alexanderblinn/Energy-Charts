from enum import Enum


class Endpoints(Enum):
    """Available endpoints for the energy-charts API."""

    # query power values
    PUBLIC_POWER = "public_power"
    PUBLIC_POWER_FORECAST = "public_power_forecast"
    TOTAL_POWER = "total_power"
    INSTALLED_POWER = "installed_power"
    FREQUENCY = "frequency"

    # query import and export values
    CBET = "cbet"  # cross border electricity trading
    CBPF = "cbpf"  # cross border physical flows

    # query price values
    PRICE = "price"

    # query renewable energy share values
    SIGNAL = "signal"  # traffic signal
    REN_SHARE_FORECAST = "ren_share_forecast"
    REN_SHARE_DAILY_AVG = "ren_share_daily_avg"
    SOLAR_SHARE = "solar_share"
    SOLAR_SHARE_DAILY_AVG = "solar_share_daily_avg"
    WIND_ONSHORE_SHARE = "wind_onshore_share"
    WIND_ONSHORE_SHARE_DAILY_AVG = "wind_onshore_share_daily_avg"
    WIND_OFFSHORE_SHARE = "wind_offshore_share"
    WIND_OFFSHORE_SHARE_DAILY_AVG = "wind_offshore_share_daily_avg"


class SubTypes(Enum):
    """Available subtypes for the energy-charts API."""

    SOLARLOG = "solarlog"  # only available for Switzerland


class ProductionType(Enum):
    """Available production types for the energy-charts API."""

    SOLAR = "solar"
    WIND_ONSHORE = "wind_onshore"
    WIND_OFFSHORE = "wind_offshore"
    LOAD = "load"


class ForecastType(Enum):
    """Available forecast types for the energy-charts API."""

    CURRENT = "current"
    INTRADAY = "intraday"
    DAY_AHEAD = "day-ahead"


class TimeSteps(Enum):
    """Available time steps for the energy-charts API."""

    # Note: currently only available for Germany

    YEARLY = "yearly"
    MONTHLY = "monthly"


class Regions(Enum):
    """Available synchronous electrical grids for the energy-charts API."""

    # Note: currently only available for UCTE (Region Continental Europe)

    UCTE = "UCTE"


class Countries(Enum):
    """Available countries for the energy-charts API (alphabetically sorted)."""

    ALBANIA = "al"
    ARMENIA = "am"
    AUSTRIA = "at"
    AZERBAIJAN = "az"
    BELARUS = "by"
    BELGIUM = "be"
    BOSNIA_HERZEGOVINA = "ba"
    CYPRUS = "cy"
    CZECH_REPUBLIC = "cz"
    DENMARK = "dk"
    ESTONIA = "ee"
    EUROPEAN = "eu"
    FINLAND = "fi"
    FRANCE = "fr"
    GEORGIA = "ge"
    GERMANY = "de"
    GREECE = "gr"
    CROATIA = "hr"
    HUNGARY = "hu"
    IRELAND = "ie"
    ITALY = "it"
    KOSOVO = "xk"
    LATVIA = "lv"
    LITHUANIA = "lt"
    LUXEMBOURG = "lu"
    MALTA = "mt"
    MOLDOVA = "md"
    MONTENEGRO = "me"
    NETHERLANDS = "nl"
    NORTH_IRELAND = "nie"
    NORTH_MACEDONIA = "mk"
    NORWAY = "no"
    POLAND = "pl"
    PORTUGAL = "pt"
    ROMANIA = "ro"
    RUSSIA = "ru"
    SERBIA = "rs"
    SLOVAK_REPUBLIC = "sk"
    SLOVENIA = "sl"
    SPAIN = "es"
    SWEDEN = "se"
    SWITZERLAND = "ch"
    TURKEY = "tr"
    UKRAINE = "ua"
    UNITED_KINGDOM = "uk"
    ALL_EUROPE = "all"


class BindingZones(Enum):
    """Available binding zones for the energy-charts API."""

    AUSTRIA = "AT"
    BELGIUM = "BE"
    SWITZERLAND = "CH"
    CZECH_REPUBLIC = "CZ"
    GERMANY_LUXEMBOURG = "DE-LU"
    GERMANY_AUSTRIA_LUXEMBOURG = "DE-AT-LU"
    DENMARK_1 = "DK1"
    DENMARK_2 = "DK2"
    FRANCE = "FR"
    HUNGARY = "HU"
    ITALY_NORTH = "IT-North"
    NETHERLANDS = "NL"
    NORWAY_2 = "NO2"
    POLAND = "PL"
    SWEDEN_4 = "SE4"
    SLOVENIA = "SI"
