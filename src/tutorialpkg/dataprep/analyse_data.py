import sys
from pathlib import Path
# Import pandas for data analysis
import pandas as pd

def describe_dataframe(df):
    """ Description of the contents of the data using Pandas dataframe functions.

            Read the data from the file and perform the following operations:
            - Display the first 5 rows of the dataframe
            - Display the shape of the dataframe
            - Display the column names
            - Display the data types of the columns
            - Display summary statistics
            - Display any missing values in the dataframe

           Parameters:
           data_file (Path): Filepath of the file in csv or excel format

    """
    # Display the shape of the dataframe
    print("\nShape of the dataframe:")
    print(df.shape)

    # Display the first 5 rows of the dataframe
    print("First 5 rows of the dataframe:")
    print(df.head())

    # Display the last 5 rows of the dataframe
    print("Last 5 rows of the dataframe:")
    print(df.tail())

    # Display the column names
    print("\nColumn names:")
    print(df.columns)

    # Display the data types of the columns
    print("\nData types of the columns:")
    print(df.dtypes)

    # Display summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Display any missing values in the dataframe
    print("Rows with missing values:")
    print(df[df.isna().any(axis=1)])

    # Print columns with missing values
    print("\nColumns with missing values:")
    print(df.isnull().sum())

if __name__ == "__main__":
    # Filepath of the csv data file
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")

    # Filepath of the Excel data file.
    paralympics_datafile_excel = Path(__file__).parent.parent.joinpath("data", "paralympics_all_raw.xlsx")

    # Filepath of the NPC codes csv data file
    npc_csv = Path(__file__).parent.parent.joinpath("data", "npc_codes.csv")

    # Read the data from the files into a Pandas dataframe. Version includes error handling for the file read
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
        events_csv_df = pd.read_csv(paralympics_datafile_csv)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    events_excel_df = pd.read_excel(paralympics_datafile_excel)
    medal_standings_df = pd.read_excel(paralympics_datafile_excel, sheet_name="medal_standings")

    #  Call the function to describe the dataframe
    describe_dataframe(events_csv_df)
    describe_dataframe(events_excel_df)
    describe_dataframe(medal_standings_df)

    # This version outputs to a text file in  the tutor_solutiom directory rather than printing to the console
    describe_output_file = Path(__file__).parent.joinpath("describe_output.txt")
    with open(describe_output_file, 'w') as f:
        # Redirect stdout to a file temporarily
        sys.stdout = f
        print('\nEVENTS .CSV DATAFRAME\n----------------------')
        describe_dataframe(events_csv_df)
        print('\nEVENTS .XLSX DATAFRAME\n----------------------')
        describe_dataframe(events_excel_df)
        print('\nMEDAL STANDINGS .XLSX DATAFRAME\n----------------------')
        describe_dataframe(medal_standings_df)
        f.close()
        # Redirect stdout back to the console
        sys.stdout = sys.__stdout__


    
