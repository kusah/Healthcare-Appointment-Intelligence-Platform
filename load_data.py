import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv("data/healthcare.csv")

# Rename column
df.rename(columns={"No-show": "No_show"}, inplace=True)

# Convert dates
df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"])
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"])

# Remove timezone info
df["ScheduledDay"] = df["ScheduledDay"].dt.tz_localize(None)
df["AppointmentDay"] = df["AppointmentDay"].dt.tz_localize(None)

engine = create_engine(
    "mysql+pymysql://root:sah123@localhost/healthcare_db"
)

# Insert in chunks
df.to_sql(
    "appointments_raw",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Data imported successfully!")
print("Rows imported:", len(df))