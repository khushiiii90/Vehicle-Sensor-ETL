import pandas as pd
import os

# Get absolute path to the current project directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input and output file paths
input_file = os.path.join(base_dir, "vehicle_data.csv")
output_file = os.path.join(base_dir, "cleaned_vehicle_data.csv")

# Load the data
df = pd.read_csv(input_file)

# --- Data Cleaning and Transformation ---
df = df.dropna()  # Remove rows with missing values
df = df.drop_duplicates()  # Remove duplicate rows

# Convert timestamp column to datetime (if it exists)
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Round numeric columns to 2 decimal places
for col in df.select_dtypes(include=['float', 'int']).columns:
    df[col] = df[col].round(2)

# --- Save cleaned data ---
df.to_csv(output_file, index=False)

print("✅ Data transformation complete! Cleaned data saved as:", output_file)
