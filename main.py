import pandas as pd
from scripts.data_cleaning import clean_data
from scripts.data_transformation import transform_data

def main():

    # 1. Load raw dataset
    df = pd.read_csv("raw_data.csv")
    print("Raw data loaded. Shape:", df.shape)

    # 2. Clean the data
    df_clean = clean_data(df)
    print("Data cleaned. Shape:", df_clean.shape)

    # 3. Transform the data
    df_transformed = transform_data(df_clean)
    print("Data transformed. New columns:", df_transformed.columns.tolist())

if __name__ == "__main__":
    main()
