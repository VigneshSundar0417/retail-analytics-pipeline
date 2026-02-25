import pandas as pd
import sqlite3
import streamlit as st
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("sales.db")

# Load mart tables
customer_df = pd.read_sql("SELECT * FROM mart_customer_revenue", conn)
product_df = pd.read_sql("SELECT * FROM mart_product_revenue", conn)
monthly_df = pd.read_sql("SELECT * FROM mart_monthly_revenue", conn)

conn.close()

# Streamlit page config
st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")
st.title("Retail Sales Analytics Dashboard")

# -----------------------------
# Monthly Revenue
# -----------------------------
st.subheader("Monthly Revenue Trend")
fig1, ax1 = plt.subplots()
ax1.plot(monthly_df["order_month"], monthly_df["revenue"], marker='o')
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue")
ax1.set_title("Monthly Revenue Trend")
plt.xticks(rotation=45)
st.pyplot(fig1)

# -----------------------------
# Top Customers
# -----------------------------
st.subheader("Top Customers by Revenue")
top_customers = customer_df.sort_values(by="revenue", ascending=False).head(10)
st.table(top_customers)

# -----------------------------
# Product Revenue
# -----------------------------
st.subheader("Product Revenue Summary")
st.bar_chart(product_df.set_index("product")["revenue"])