import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from textblob import TextBlob

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "CodeAlpha_Sentiment_Reviews.csv"

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    page_icon="😊",
    layout="wide"
)

# Title
st.title("😊 Customer Sentiment Analysis Dashboard")
st.write("CodeAlpha Data Analytics Internship - Task 3")

# Load dataset
df = pd.read_csv(DATA_PATH)

# -----------------------------
# Sentiment Analysis
# -----------------------------

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


df["Sentiment"] = df["Review"].apply(get_sentiment)

# -----------------------------
# Sidebar Filter
# -----------------------------

st.sidebar.header("🔎 Filters")

products = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

sentiments = st.sidebar.multiselect(
    "Select Sentiment",
    options=["Positive", "Neutral", "Negative"],
    default=["Positive", "Neutral", "Negative"]
)

# Apply filters
filtered_df = df[
    (df["Product"].isin(products)) &
    (df["Sentiment"].isin(sentiments))
]

# -----------------------------
# KPI Metrics
# -----------------------------

st.subheader("📌 Key Metrics")

total_reviews = len(filtered_df)
positive_reviews = len(filtered_df[filtered_df["Sentiment"] == "Positive"])
negative_reviews = len(filtered_df[filtered_df["Sentiment"] == "Negative"])
neutral_reviews = len(filtered_df[filtered_df["Sentiment"] == "Neutral"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("📝 Total Reviews", total_reviews)
col2.metric("😊 Positive", positive_reviews)
col3.metric("😞 Negative", negative_reviews)
col4.metric("😐 Neutral", neutral_reviews)

st.divider()

# -----------------------------
# Sentiment Distribution
# -----------------------------

st.subheader("📊 Sentiment Distribution")

sentiment_counts = filtered_df["Sentiment"].value_counts()

fig, ax = plt.subplots()

sentiment_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Sentiment")
ax.set_ylabel("Number of Reviews")
ax.set_title("Sentiment Distribution")

plt.xticks(rotation=0)

st.pyplot(fig)

# -----------------------------
# Sentiment Pie Chart
# -----------------------------

st.subheader("🥧 Sentiment Percentage")

fig, ax = plt.subplots()

sentiment_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)

# -----------------------------
# Product-wise Sentiment
# -----------------------------

st.subheader("📈 Sentiment by Product")

product_sentiment = pd.crosstab(
    filtered_df["Product"],
    filtered_df["Sentiment"]
)

fig, ax = plt.subplots(figsize=(12, 6))

product_sentiment.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Product")
ax.set_ylabel("Number of Reviews")
ax.set_title("Sentiment Distribution by Product")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# -----------------------------
# Rating Distribution
# -----------------------------

st.subheader("⭐ Rating Distribution")

rating_counts = filtered_df["Rating"].value_counts().sort_index()

fig, ax = plt.subplots()

rating_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Rating")
ax.set_ylabel("Number of Reviews")
ax.set_title("Customer Rating Distribution")

plt.xticks(rotation=0)

st.pyplot(fig)

# -----------------------------
# Reviews Table
# -----------------------------

st.subheader("📋 Customer Reviews")

st.dataframe(
    filtered_df[
        ["Review_ID", "Product", "Review", "Rating", "Sentiment"]
    ],
    use_container_width=True
)