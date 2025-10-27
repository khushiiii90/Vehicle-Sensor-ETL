import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# --- Page Setup ---
st.set_page_config(page_title="Vehicle Sensor Dashboard", page_icon="🚗", layout="wide")

# --- Auto-refresh ---
st.markdown("### 🔄 Live Vehicle Data Dashboard")
st.caption("Refreshing automatically every 10 seconds...")

# Auto-refresh every 10 seconds (10000 ms)
st_autorefresh(interval=10000, key="vehicle_dashboard_refresh")

# --- Load Data from SQLite ---
conn = sqlite3.connect("vehicle_data.db")
df = pd.read_sql_query("SELECT * FROM vehicle_data", conn)
conn.close()

if df.empty:
    st.warning("No data found in database yet.")
else:
    # --- Vehicle Filter ---
    vehicle_ids = sorted(df["vehicle_id"].unique())
    selected_vehicles = st.multiselect(
        "Select Vehicle(s):",
        options=vehicle_ids,
        default=vehicle_ids[:3] if len(vehicle_ids) >= 3 else vehicle_ids
    )

    # Filter data based on selection
    filtered_df = df[df["vehicle_id"].isin(selected_vehicles)]

    # --- Display Filtered Data ---
    st.subheader("📄 Filtered Vehicle Data")
    st.dataframe(filtered_df.tail(10))  # show latest entries

    # --- Speed over Time ---
    st.subheader("📈 Speed over Time")
    fig_speed = px.line(
        filtered_df,
        x="timestamp",
        y="speed",
        color="vehicle_id",
        title="Speed Over Time"
    )
    st.plotly_chart(fig_speed, use_container_width=True)

    # --- Fuel vs Engine Temp ---
    st.subheader("⛽ Fuel vs Engine Temperature")
    fig_fuel = px.scatter(
        filtered_df,
        x="fuel_level",
        y="engine_temp",
        color="vehicle_id",
        title="Fuel Level vs Engine Temperature",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig_fuel, use_container_width=True)

    # --- GPS Map ---
    st.subheader("🗺️ Vehicle Locations")
    fig_map = px.scatter_mapbox(
        filtered_df,
        lat="gps_lat",
        lon="gps_long",
        color="vehicle_id",
        hover_name="vehicle_id",
        zoom=3,
        mapbox_style="open-street-map"
    )
    st.plotly_chart(fig_map, use_container_width=True)

# --- Footer ---
st.info("⏳ Auto-refreshes every 10 seconds.")
