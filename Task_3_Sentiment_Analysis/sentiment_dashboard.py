import streamlit as st
import pandas as pd
from pathlib import Path
from textblob import TextBlob

# Find the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# Dataset path
DATA_PATH = BASE_DIR / "data" / "CodeAlpha_Sentiment_Reviews.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    page_icon="😊",
    layout="wide"
)

st.title("😊 Customer Sentiment Analysis Dashboard")
st.write("CodeAlpha Data Analytics Internship - Task 3")

# Sentiment function
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

st.subheader("📊 Sentiment Distribution")
sentiment_counts = df["Sentiment"].value_counts()

st.bar_chart(sentiment_counts)

st.subheader("📝 Reviews with Sentiment")
st.dataframe(
    df[["Review_ID", "Product", "Review", "Rating", "Sentiment"]],
    use_container_width=True
)