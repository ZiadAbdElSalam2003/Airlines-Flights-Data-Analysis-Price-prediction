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

* Source: [Kaggle – Airline Dataset](https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data)
* Data includes information on flights: ticket price, duration, stops, travel class etc...

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

![Dashboard 1](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/dashboard1.png)
![Dashboard 2](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/dashboard2.png)
![Dashboard 3](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/dashboard3.png)
![Dashboard 4](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/dashboard4.png)

### 4. Machine Learning Models

We trained and compared two ML models:

* **Decision Tree (DT)**
* **LightGBM (LGBM)**

**Key Findings:**

* DT required encoding & more preprocessing, provided baseline performance.
* LGBM was more efficient, required less preprocessing, and achieved higher accuracy.

📸 Model Performance:

* Decision Tree accuracy vs depth plot → ![DT Performance](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/dt-performance.png)
* LightGBM accuracy vs depth plot → ![LGBM Performance](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/LGBM-performance.png)

**Final Results:**

* ![Final Accuracy](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/final-acc.png)
* Metrics (MAE, MSE, Train R², Test R²):

  ```
  MAE: 1601.19
  MSE: 8386989.59
  Train R²: 0.9862
  Test R²: 0.9837
  ```

### 5. Deployment (Streamlit App)

To make predictions accessible to users, we deployed a simple **Streamlit web application**.
Users can input flight details and instantly get predicted ticket prices.

📸 App Screenshot:
![Streamlit App](https://github.com/ZiadAbdElSalam2003/Airlines-Flights-Data-Analysis-Price-prediction/blob/1248d8cb2fa070308a34e865d168c83b81d2974f/assets/streamlit-app.png)

---

## 👤 My Role

* Led the **Machine Learning part** end-to-end: preprocessing, model development, evaluation, and optimization.
* Built and compared the ML models (**Decision Tree vs LightGBM**), achieving higher accuracy with LightGBM.
* Developed and deployed the **Streamlit web application** for user-friendly predictions.
* Contributed to the **Power BI dashboards**, assisting in structuring and designing the final layout.

---

## 👥 Team Members

* Ziad Mohamed Abd El-Salam (me)
* Wafaa Galal
* Rahaf Mohamed
* Shaimaa Sayed
* Omar Gamal

---


## ⚡ Tools & Technologies

* **Programming:** Python, Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Power BI
* **Machine Learning:** Scikit-learn, LightGBM
* **Deployment:** Streamlit
