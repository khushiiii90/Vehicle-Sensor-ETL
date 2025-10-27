import pandas as pd

def clean_data(input_file="raw_sensor_data.csv", output_file="cleaned_sensor_data.csv"):
    """Clean the raw vehicle sensor data"""
    df = pd.read_csv(input_file)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Remove impossible values (for example, speed < 0 or > 250)
    df = df[(df["speed_kmph"] >= 0) & (df["speed_kmph"] <= 250)]

    # Save the cleaned data
    df.to_csv(output_file, index=False)
    print("✅ Data cleaned and saved as 'cleaned_sensor_data.csv'")

if __name__ == "__main__":
    clean_data()
