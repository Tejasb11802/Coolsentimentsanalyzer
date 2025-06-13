import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Customer Sentiment Explorer", layout="centered")

st.title("Customer Sentiment Explorer")
st.write("Analyze the sentiment of your customer feedback, social media posts, or general text input.")

# Input text box
user_input = st.text_area("Enter text to analyze:")

# Sentiment analysis logic
if st.button("Analyze Sentiment"):
    if user_input:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity

        st.markdown("### 🔍 Sentiment Results")
        st.write(f"**Polarity:** {polarity:.2f} (−1 = Negative, +1 = Positive)")
        st.write(f"**Subjectivity:** {subjectivity:.2f} (0 = Objective, 1 = Subjective)")

        if polarity > 0:
            st.success("Overall Sentiment: Positive")
        elif polarity < 0:
            st.error("Overall Sentiment: Negative")
        else:
            st.info("Overall Sentiment: Neutral")
    else:
        st.warning("Please enter some text to analyze.")
