# Vehicle-Sensor-ETL
This project simulates a real-time vehicle data monitoring system using an ETL (Extract, Transform, Load) pipeline. It processes sensor data such as vehicle speed, engine temperature, fuel level, and GPS coordinates, cleaning and loading it into a SQLite database, then visualizing it on an interactive dashboard.

1) Overview
- **Extract:** Simulated raw sensor data from vehicles (speed, fuel, engine temp, GPS).  
- **Transform:** Cleaned and structured using Python ETL scripts.  
- **Load:** Stored into an SQLite database (`vehicle_data.db`).  
- **Visualize:** Real-time dashboard built using Streamlit and Plotly.

2)  Tech Stack
- Python  
- Pandas  
- SQLite  
- Plotly  
- Streamlit  

3) Features
- Live data refresh every 10 seconds  
- Interactive plots for speed, temperature, and fuel  
- Vehicle GPS visualization on a map  
- ETL automation pipeline  

4) Setup
- Clone the repository  
- Install dependencies:  
   ```bash
   pip install -r requirements.txt
- Run the ETL pipeline:  
   ```bash
   python run_etl.py
- ```bash
  streamlit run dashboard.py

