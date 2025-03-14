# AI-Powered Guest Experience Personalization System for Hospitality

## Overview
This project is an **AI-powered system** designed to enhance guest experiences in the hospitality industry. It integrates **data analytics**, **machine learning**, and **real-time feedback mechanisms** to provide personalized services, predict guest preferences, and improve operational efficiency. The system is divided into four modules, each addressing a specific aspect of guest experience management.

---

## Modules

### **Module 1: Dining Data Analysis & Prediction**
- **Objective:** Analyze hotel dining data and predict customer dining preferences using **XGBoost**.
- **Key Features:**
  - Data ingestion from **MongoDB** and Excel (`dining_info.xlsx`).
  - Preprocessing and feature engineering (e.g., stay duration, order time attributes, customer loyalty).
  - Training an **XGBoost Classifier** to predict preferred dishes.
  - Evaluation using accuracy and log loss metrics.
  - Saving the trained model and encoders for future use.
- **Outputs:**
  - Model file: `xgb_model_dining.pkl`
  - Encoders: `encoder.pkl`, `label_encoder.pkl`
  - Feature importance plot.

---

### **Module 2: Hotel Booking System with Machine Learning**
- **Objective:** Predict hotel booking outcomes using **XGBoost** and integrate predictions into a **Streamlit** application.
- **Key Features:**
  - Data extraction from **MongoDB**.
  - Preprocessing (missing value handling, categorical encoding, normalization).
  - Training an **XGBoost Classifier** for booking status prediction.
  - Deployment of the model in a **Streamlit** interface for real-time predictions.
- **Outputs:**
  - Model file: `hotel_booking_model.pkl`
  - Streamlit-based booking prediction system.

---

### **Module 3: Customer Review Submission & Sentiment Analysis**
- **Objective:** Manage customer reviews, perform sentiment analysis, and notify managers of negative feedback.
- **Key Features:**
  - Review submission via **Streamlit**.
  - Sentiment analysis using **TextBlob**.
  - Data storage in `reviews_data.xlsx`.
  - Email alerts for negative reviews (sentiment score < -0.2).
- **Outputs:**
  - Updated Excel file with reviews and sentiment scores.
  - Email notifications for negative reviews.

---

### **Module 4: Hotel Data Analytics Dashboard**
- **Objective:** Provide a comprehensive analytics dashboard for hotel bookings, dining insights, and customer reviews.
- **Key Features:**
  - Interactive visualizations using **Plotly** and **Matplotlib**.
  - Data filtering options (date range, cuisine, rating).
  - Insights into booking trends, dining preferences, and customer sentiment.
  - Word cloud for customer feedback analysis.
- **Outputs:**
  - Streamlit-based dashboard with real-time data visualizations.

---

## Technologies Used
- **Programming Language:** Python
- **Data Storage:** MongoDB
- **Machine Learning:** XGBoost, Scikit-learn
- **Visualization:** Plotly, Matplotlib, WordCloud
- **Web Framework:** Streamlit
- **Sentiment Analysis:** TextBlob
- **Data Manipulation:** Pandas

---

## Installation
### Prerequisites
Ensure you have Python installed. Install the required dependencies using:
```bash
pip install pymongo pandas xgboost scikit-learn joblib matplotlib streamlit openpyxl textblob plotly wordcloud
```

---

## Running the System
1. **Module 1: Dining Data Analysis & Prediction**
   ```bash
   python module1_script.py
   ```

2. **Module 2: Hotel Booking System**
   ```bash
   streamlit run module2_script.py
   ```

3. **Module 3: Customer Review System**
   ```bash
   streamlit run module3.py
   ```

4. **Module 4: Hotel Data Analytics Dashboard**
   ```bash
   streamlit run module4.py
   ```

---

## Configuration
- **MongoDB Connection:** Update the connection string in each module to connect to your MongoDB instance.
- **Email Alerts:** Configure `sender_email` and `sender_password` in Module 3 for email functionality.
- **File Paths:** Ensure file paths for Excel files (`dining_info.xlsx`, `reviews_data.xlsx`) are correct.



## Summary
This system leverages **AI and data analytics** to transform guest experiences in the hospitality industry. By combining **predictive modeling**, **real-time feedback**, and **interactive dashboards**, it enables hotels to deliver personalized services, optimize operations, and improve customer satisfaction.
