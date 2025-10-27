import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("vehicle_data.db")

# 1️⃣ Average speed per vehicle
avg_speed = pd.read_sql_query("""
SELECT vehicle_id, ROUND(AVG(speed), 2) AS avg_speed
FROM vehicle_data
GROUP BY vehicle_id
""", conn)
print("\n🚗 Average Speed per Vehicle:\n", avg_speed.head())

# 2️⃣ Detect engine overheating
overheat = pd.read_sql_query("""
SELECT * FROM vehicle_data
WHERE engine_temp > 100
""", conn)
print("\n🔥 Overheating Vehicles:\n", overheat.head())

# 3️⃣ Low fuel alerts
low_fuel = pd.read_sql_query("""
SELECT * FROM vehicle_data
WHERE fuel_level < 30
""", conn)
print("\n⛽ Low Fuel Alerts:\n", low_fuel.head())

conn.close()
