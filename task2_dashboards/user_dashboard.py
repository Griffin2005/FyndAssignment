import streamlit as st
from llm_utils import call_llm
from storage import save_review


st.set_page_config(page_title="User Feedback", layout="centered")


st.title("📝 Submit Your Review")

rating = st.selectbox("Select Rating", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")

if st.button("Submit Review"):
    if review.strip() == "":
        st.warning("Please write a review.")
    else:
        user_prompt = f"""
        You are a friendly customer support assistant.
        Respond politely and empathetically to the following review.

        Rating: {rating}
        Review: {review}
        """

        ai_response = call_llm(user_prompt)

        summary_prompt = f"""
        Summarize the following customer review in one sentence.

        Review:
        {review}
        """

        ai_summary = call_llm(summary_prompt)

        action_prompt = f"""
        Suggest one recommended business action based on this review.

        Review:
        {review}
        """

       
        recommended_action = call_llm(action_prompt)

        save_review(
            rating,
            review,
            ai_response,
            ai_summary,
            recommended_action
        )

        st.success("Review submitted successfully!")
        st.subheader("🤖 AI Response")
        st.write(ai_response)
