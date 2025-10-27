import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("vehicle_data.db")

# Read all data
df = pd.read_sql_query("SELECT * FROM vehicle_data LIMIT 10;", conn)

print("🚗 Sample Data from Database:")
print(df)

conn.close()
