import pandas as pd


def make_dataframe(response: dict) -> pd.DataFrame:
    """
    Converts an API response dictionary into a pandas DataFrame.
    Merges data from 'production_types' and 'countries' keys by timestamp.

    Parameters:
        response (dict): The API response to parse.

    Returns:
        pd.DataFrame: A DataFrame with aligned data and timestamps.
    """
    if not response:
        raise ValueError("The response is empty or invalid.")

    # Convert 'unix_seconds' to timestamps
    timestamps = (
        pd.to_datetime(response.get("unix_seconds", []), unit="s")
        if "unix_seconds" in response
        else None
    )

    # Initialize a DataFrame with timestamps
    df = pd.DataFrame({"timestamp": timestamps}) if timestamps is not None else pd.DataFrame()

    # Handle 'production_types'
    if "production_types" in response:
        for entry in response["production_types"]:
            if isinstance(entry, dict):
                name = entry.get("name")  # Use 'name' as column name
                data = entry.get("data", [])
                temp_df = pd.DataFrame({"timestamp": timestamps, name: data})
                df = pd.merge(df, temp_df, on="timestamp", how="outer")

    # Handle 'countries'
    if "countries" in response:
        for entry in response["countries"]:
            if isinstance(entry, dict):
                name = entry.get("name")  # Use 'name' as column name
                data = entry.get("data", [])
                temp_df = pd.DataFrame({"timestamp": timestamps, name: data})
                df = pd.merge(df, temp_df, on="timestamp", how="outer")

    # Add other fields
    other_columns = {
        k: v
        for k, v in response.items()
        if k not in {"production_types", "countries", "unix_seconds"}
    }
    for key, values in other_columns.items():
        if isinstance(values, list):  # Align lists with timestamps
            temp_df = pd.DataFrame({"timestamp": timestamps, key: values})
            df = pd.merge(df, temp_df, on="timestamp", how="outer")
        else:  # Add scalar values directly
            df[key] = values

    # Ensure the DataFrame is sorted by timestamp
    if "timestamp" in df.columns:
        df = df.sort_values(by="timestamp")

    return df
