import pandas as pd
import sqlite3

def load_data_to_db(csv_file="cleaned_sensor_data.csv", db_name="vehicle_data.db"):
    """Load cleaned data into SQLite database"""
    # Read CSV
    df = pd.read_csv(csv_file)

    # Connect to database (creates one if it doesn’t exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicle_data (
            timestamp TEXT,
            vehicle_id TEXT,
            speed_kmph INTEGER,
            engine_temp_c REAL,
            fuel_level_percent REAL
        )
    """)

    # Insert data
    df.to_sql("vehicle_data", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()
    print("✅ Data loaded successfully into 'vehicle_data.db' database")

if __name__ == "__main__":
    load_data_to_db()
