import streamlit as st
from task2_dashboards.storage import read_reviews
from collections import Counter

st.set_page_config(page_title="Admin Dashboard", layout="wide")

reviews = read_reviews()

st.title("📊 Admin Dashboard")

if len(reviews) == 0:
    st.info("No reviews yet.")
    st.stop()

# --- BASIC METRICS ---
ratings = [int(r["rating"]) for r in reviews]

st.metric("Total Reviews", len(reviews))
st.metric("Average Rating", round(sum(ratings) / len(ratings), 2))

negative_count = sum(1 for r in ratings if r <= 2)
negative_percentage = (negative_count / len(ratings)) * 100

st.metric("Negative Reviews (%)", round(negative_percentage, 2))

st.divider()

rating_counts = Counter(ratings)

st.subheader("⭐ Rating Distribution")
st.bar_chart(rating_counts)

st.divider()
st.subheader("📋 All Reviews")

for r in reviews[::-1]:
    st.markdown(f"### ⭐ Rating: {r['rating']}")
    st.write("**User Review:**", r["review"])
    st.write("**AI Summary:**", r["ai_summary"])
    st.write("**Recommended Action:**", r["recommended_action"])
    st.caption(f"🕒 {r['timestamp']}")
    st.divider()
