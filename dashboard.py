import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales.db")

df = pd.read_sql(
    "SELECT * FROM mart_monthly_revenue",
    conn
)

plt.figure(figsize=(8,5))

plt.plot(df["order_month"], df["revenue"])

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save dashboard image instead of showing
plt.savefig("dashboard_report.png")

print("Dashboard saved as dashboard_report.png")

conn.close()