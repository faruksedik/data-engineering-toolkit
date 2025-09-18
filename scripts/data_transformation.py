import pandas as pd

def transform_data(df):
    """
    Transforms the DataFrame by:
    - Converting order_date to datetime
    - Ensuring quantity_sold is int
    - Ensuring price is float
    - Creating a new column 'total' = quantity * price
    """
    # Convert data types
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity_sold"] = df["quantity_sold"].astype(int)
    df["price"] = df["price"].astype(float)

    # Create new column
    df["total"] = df["quantity_sold"] * df["price"]

    return df