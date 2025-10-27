import random
import pandas as pd
from datetime import datetime

def generate_sensor_data(num_records=100):
    """Generate fake vehicle sensor data"""
    data = {
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(num_records)],
        "vehicle_id": [f"VH{random.randint(1000, 9999)}" for _ in range(num_records)],
        "speed_kmph": [random.randint(0, 180) for _ in range(num_records)],
        "engine_temp_c": [random.uniform(60, 120) for _ in range(num_records)],
        "fuel_level_percent": [random.uniform(0, 100) for _ in range(num_records)]
    }

    df = pd.DataFrame(data)
    df.to_csv("raw_sensor_data.csv", index=False)
    print("✅ Sensor data generated and saved as 'raw_sensor_data.csv'")

if __name__ == "__main__":
    generate_sensor_data()
