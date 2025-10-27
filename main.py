from data_generator import generate_sensor_data
from data_cleaner import clean_data
from data_loader import load_data_to_db

def main():
    print("🚗 Starting Vehicle Sensor ETL Pipeline...\n")

    # Step 1: Generate fake data
    generate_sensor_data()

    # Step 2: Clean the data
    clean_data()

    # Step 3: Load into database
    load_data_to_db()

    print("\n🎯 ETL Pipeline completed successfully!")

if __name__ == "__main__":
    main()
