import pandas as pd

def load_data(df, output_file):
    """
    Saves the DataFrame to a CSV file.
    """
    df.to_csv(output_file, index=False)
    print("Data saved to", output_file)