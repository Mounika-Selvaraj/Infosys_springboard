import streamlit as st
import pandas as pd
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
from textblob import TextBlob

# Load or create an Excel file
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_excel(file_path)
    else:
        return pd.DataFrame(columns=["review_id", "customer_id", "review_date", "Review", "Rating", "sentiment_score"])

def save_data(data, file_path):
    data.to_excel(file_path, index=False)

# Sentiment analysis function
def analyze_sentiment(review_text):
    return TextBlob(review_text).sentiment.polarity  # Sentiment score between -1 and 1

# Function to send email via Gmail SMTP
def send_email(manager_email, review_text, customer_id, rating, sentiment_score):
    sender_email = "mounika9385742197@gmail.com"  # Replace with your Gmail
    sender_password = "bxexdtqvaqgebggo"  # Replace with your App Password

    subject = "⚠️ Negative Review Alert!"
    body = f"""
    Dear Manager,

    A new negative review has been submitted.

    📌 **Customer ID:** {customer_id}
    ⭐ **Rating:** {rating}/10
    📝 **Review:** {review_text}
    📉 **Sentiment Score:** {sentiment_score:.2f}

    Please take necessary action.

    Regards,
    Automated Review System
    """

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = manager_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        st.success("📩 Email sent successfully to the manager!")
    except Exception as e:
        st.error(f"⚠️ Email sending failed: {e}")

# Main app function
def main():
    file_path = "reviews_data.xlsx"
    manager_email = "mounika82005@gmail.com"  # Replace with actual manager's email
    
    st.title("📢 Customer Review Submission Form 📝")
    
    review_id = st.text_input("🔢 Review ID")
    customer_id = st.text_input("🆔 Customer ID")
    review_text = st.text_area("💬 Review")
    rating = st.slider("⭐ Rating", 1, 10, 3)
    
    if st.button("✅ Submit Review"):
        if review_id and customer_id and review_text:
            review_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sentiment_score = analyze_sentiment(review_text)
            
            new_data = pd.DataFrame({
                "review_id": [review_id],
                "customer_id": [customer_id],
                "review_date": [review_date],
                "Review": [review_text],
                "Rating": [rating],
                "sentiment_score": [sentiment_score]
            })
            
            data = load_data(file_path)
            data = pd.concat([data, new_data], ignore_index=True)
            save_data(data, file_path)
            st.success("🎉 Review submitted successfully!")
            
            st.subheader("📊 Sentiment Analysis")
            st.write(f"📉 Sentiment Score: {sentiment_score:.2f}")
            
            # Automatically trigger email if sentiment is negative
            if sentiment_score < -0.2:
                send_email(manager_email, review_text, customer_id, rating, sentiment_score)
                st.warning("⚠️ Negative review detected! Manager has been notified.")

            st.subheader("📊 Updated Reviews Data")
            st.dataframe(data)
        else:
            st.error("⚠️ Please fill all the required fields.")

if __name__ == "__main__":
    main()
