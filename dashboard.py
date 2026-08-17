import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Sales Analytics Dashboard")
st.write("CodeAlpha Data Analytics Internship Project")

# Load Dataset
df = pd.read_csv("data/CodeAlpha_Sales_100_Rows.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar Filters
st.sidebar.header("🔎 Filters")

categories = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

# Apply Filters
filtered_df = df[
    (df["Category"].isin(categories)) &
    (df["Region"].isin(regions))
]

# KPI Metrics
st.subheader("📌 Key Performance Indicators")

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_quantity = filtered_df["Quantity"].sum()
total_orders = filtered_df["Order_ID"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"₹{total_sales:,.2f}")
col2.metric("📈 Total Profit", f"₹{total_profit:,.2f}")
col3.metric("📦 Total Quantity", total_quantity)
col4.metric("🧾 Total Orders", total_orders)

st.divider()

# Sales by Category - Bar Chart
st.subheader("📊 Sales by Category")

category_sales = filtered_df.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots()
category_sales.plot(kind="bar", ax=ax)

ax.set_xlabel("Category")
ax.set_ylabel("Sales")
ax.set_title("Sales by Category")

plt.xticks(rotation=0)

st.pyplot(fig)

# Sales Distribution - Pie Chart
st.subheader("🥧 Sales Distribution by Category")

fig, ax = plt.subplots()

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)

# Daily Sales Trend - Line Chart
st.subheader("📈 Daily Sales Trend")

daily_sales = filtered_df.groupby("Date")["Sales"].sum()

fig, ax = plt.subplots()

daily_sales.plot(
    kind="line",
    marker="o",
    ax=ax
)

ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title("Daily Sales Trend")

plt.xticks(rotation=45)

st.pyplot(fig)

# Sales vs Profit - Scatter Plot
st.subheader("🔵 Sales vs Profit")

fig, ax = plt.subplots()

ax.scatter(
    filtered_df["Sales"],
    filtered_df["Profit"]
)

ax.set_xlabel("Sales")
ax.set_ylabel("Profit")
ax.set_title("Sales vs Profit")

st.pyplot(fig)

# Data Table
st.subheader("📋 Filtered Sales Data")

st.dataframe(filtered_df, use_container_width=True)