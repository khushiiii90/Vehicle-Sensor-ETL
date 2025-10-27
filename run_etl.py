import os

# Step 1: Extract
print("🚀 Running extract step...")
os.system("python etl/extract.py")

# Step 2: Transform
print("⚙️ Running transform step...")
os.system("python etl/transform.py")

# Step 3: Load
print("📦 Running load step...")
os.system("python etl/load.py")

print("✅ ETL pipeline completed successfully!")
