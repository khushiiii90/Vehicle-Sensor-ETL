import pandas as pd
import sqlite3
import os

# Input file (cleaned data in the main folder)
input_file = os.path.join(os.path.dirname(__file__), "..", "cleaned_vehicle_data.csv")

# Database file (in main folder)
db_file = os.path.join(os.path.dirname(__file__), "..", "vehicle_data.db")

# Normalize paths (to handle .. correctly)
input_file = os.path.abspath(input_file)
db_file = os.path.abspath(db_file)

# Load the cleaned data
df = pd.read_csv(input_file)

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect(db_file)

# Load data into table named 'vehicle_data'
df.to_sql("vehicle_data", conn, if_exists="replace", index=False)

# Commit and close
conn.commit()
conn.close()

print("✅ Data loaded successfully into database:", db_file)
