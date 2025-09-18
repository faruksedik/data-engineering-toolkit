import pandas as pd

def clean_data(df):
    """
    Cleans the DataFrame:
    - Removes duplicate rows
    - Fills missing product names with 'Unknown'
    """
    # remove duplicates
    df = df.drop_duplicates() 

    # fill missing values
    df["product"] = df["product"].fillna("Unknown")  

    return df