import csv
import random
import time
from datetime import datetime

# Simulate sensor data
def generate_sensor_data():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vehicle_id": random.randint(1000, 9999),
        "speed": round(random.uniform(20, 120), 2),
        "engine_temp": round(random.uniform(60, 120), 2),
        "fuel_level": round(random.uniform(10, 100), 2),
        "gps_lat": round(random.uniform(8.5, 37.6), 6),
        "gps_long": round(random.uniform(68.7, 97.25), 6)
    }

def extract_data(filename="vehicle_data.csv", num_records=100):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=[
            "timestamp", "vehicle_id", "speed", "engine_temp", "fuel_level", "gps_lat", "gps_long"
        ])
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow(generate_sensor_data())
            time.sleep(0.05)

if __name__ == "__main__":
    extract_data()
    print("✅ Data extraction completed! CSV file generated.")
