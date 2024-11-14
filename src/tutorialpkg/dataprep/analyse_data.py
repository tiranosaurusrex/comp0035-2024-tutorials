from pathlib import Path
# Import pandas for data analysis
import pandas as pd

def describe_data(df):
    """Prints information about the DataFrame.
    
    Parameters:
    df (pandas.DataFrame): Data to describe.
    """
    print(df.info())  # Displays summary information about the DataFrame
    print(df.describe())  # Provides statistics for numeric columns 

if __name__ == '__main__':
    # Define the path for each file
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
    paralympics_datafile_excel = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")


     # Load CSV file
    events_df = pd.read_csv(paralympics_datafile_csv)

    # Load first sheet from Excel file
    excel_df = pd.read_excel(paralympics_datafile_excel, sheet_name=0)

    # Load second sheet (named 'medal_standings') from Excel file
    medal_standings_df = pd.read_excel(paralympics_datafile_excel, sheet_name='medal_standings')
    
