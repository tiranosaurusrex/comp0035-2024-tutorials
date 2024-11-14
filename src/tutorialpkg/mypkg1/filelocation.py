from pathlib import Path

if __name__ == "__main__":
    # Locate the data file relative to this code file's location
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
    
    # Check if the file exists and print the result
    if paralympics_datafile_csv.exists(): 
        print(f"Data file found: {paralympics_datafile_csv}")
    else:
        print("Data file not found")