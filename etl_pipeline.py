import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect("sales.db")

# ---------------------------
# RAW LAYER
# ---------------------------

df = pd.read_csv("sales_raw.csv")

df.to_sql(
    "sales_raw",
    conn,
    if_exists="replace",
    index=False
)

print("Raw data loaded successfully!")

# ---------------------------
# STAGING LAYER
# ---------------------------

df["order_date"] = pd.to_datetime(df["order_date"])
df["revenue"] = df["quantity"] * df["price"]
df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

df.to_sql(
    "sales_staging",
    conn,
    if_exists="replace",
    index=False
)

print("Staging table created successfully!")

# ---------------------------
# READ STAGING DATA AFTER WRITE
# ---------------------------

df_staging = pd.read_sql(
    "SELECT * FROM sales_staging",
    conn
)

# ---------------------------
# MART LAYER
# ---------------------------

# Customer mart
customer_mart = df_staging.groupby(
    ["customer_id", "customer_name"]
)["revenue"].sum().reset_index()

customer_mart.to_sql(
    "mart_customer_revenue",
    conn,
    if_exists="replace",
    index=False
)

print("Customer revenue mart created!")

# Product mart
product_mart = df_staging.groupby(
    ["product", "category"]
)["revenue"].sum().reset_index()

product_mart.to_sql(
    "mart_product_revenue",
    conn,
    if_exists="replace",
    index=False
)

print("Product revenue mart created!")

# Monthly mart
monthly_mart = df_staging.groupby(
    ["order_month"]
)["revenue"].sum().reset_index()

monthly_mart.to_sql(
    "mart_monthly_revenue",
    conn,
    if_exists="replace",
    index=False
)

print("Monthly revenue mart created!")

# Close connection
conn.close()