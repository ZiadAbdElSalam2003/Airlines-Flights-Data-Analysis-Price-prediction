# ✈️ Airline Flight Analysis and Price Prediction

## 📌 Overview

This project is part of the **Advanced Data Analytics Track** at the National Telecommunication Institute (NTI).
The goal of this project is to **analyze airlines flight data** and **predict ticket prices** using machine learning models.

We explored multiple factors such as:

* Ticket prices
* Flight duration
* Number of stops
* Travel class

The project also includes **interactive dashboards** for insights and a **Streamlit web app** for real-time price predictions.

---

## 📂 Dataset

* Source: [Kaggle – Airline Dataset](https://www.kaggle.com/)
* Data includes information on flights: ticket price, duration, stops, and travel class.
* Preprocessing steps:
  • Handling missing values
  • Encoding categorical features
  • Feature scaling & transformations

---

## 🛠 Project Workflow

### 1. Data Cleaning & Preprocessing

* Handled missing and inconsistent data.
* Feature engineering for stops, duration, and travel class.

### 2. Exploratory Data Analysis (EDA)

* Extracted key insights about pricing patterns.
* Visualized trends and distributions using **Matplotlib & Seaborn**.

### 3. Interactive Dashboards (Power BI)

We built **4 dashboards** to summarize insights:

1. **Airline Flights Overview**
2. **Airline Flights Price**
3. **Airline Flights Duration**
4. **Passenger Decision Support**

📸 Screenshots:
![Dashboard 1](assets/dashboard_overview.png)
![Dashboard 2](assets/dashboard_price.png)
![Dashboard 3](assets/dashboard_duration.png)
![Dashboard 4](assets/dashboard_decision.png)

### 4. Machine Learning Models

We trained and compared two ML models:

* **Decision Tree (DT)**
* **LightGBM (LGBM)**

**Key Findings:**

* DT required encoding & more preprocessing, provided baseline performance.
* LGBM was more efficient, required less preprocessing, and achieved higher accuracy.

📸 Model Performance:

* Decision Tree accuracy vs depth plot → ![DT Performance](assets/dt_performance.png)
* LightGBM accuracy vs depth plot → ![LGBM Performance](assets/lgbm_performance.png)

**Final Results:**

* Accuracy: ![Final Accuracy](assets/final_accuracy.png)
* Metrics (MAE, MSE, Train R², Test R²):

  ```
  MAE: X.XX
  MSE: X.XX
  Train R²: X.XX
  Test R²: X.XX
  ```

### 5. Deployment (Streamlit App)

To make predictions accessible to users, we deployed a simple **Streamlit web application**.
Users can input flight details and instantly get predicted ticket prices.

📸 App Screenshot:
![Streamlit App](assets/streamlit_app.png)

---

## 👤 My Role

* Led the **Machine Learning part** end-to-end: preprocessing, model development, evaluation, and optimization.
* Built and compared the ML models (**Decision Tree vs LightGBM**), achieving higher accuracy with LightGBM.
* Developed and deployed the **Streamlit web application** for user-friendly predictions.
* Contributed to the **Power BI dashboards**, assisting in structuring and designing the final layout.

---

## 👥 Team Members

* Zyad Mohamed Abd El-Salam
* Wafaa Galal
* Rahaf Mohamed
* Shaimaa Sayed
* Omar Gamal

---

## 🙏 Acknowledgments

Special thanks to **Eng. Arwa Esam** for her continuous support, valuable knowledge, and guidance throughout the program.

---

## ⚡ Tools & Technologies

* **Programming:** Python, Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Power BI
* **Machine Learning:** Scikit-learn, LightGBM
* **Deployment:** Streamlit
