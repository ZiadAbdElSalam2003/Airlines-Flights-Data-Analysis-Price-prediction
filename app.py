import streamlit as st
import pickle
import pandas as pd

# Load the trained LightGBM model
model = pickle.load(open("flight_price_prediction_model.pkl", "rb"))

st.set_page_config(page_title="Flight Price Predictor", page_icon="✈️", layout="centered")

st.title("✈️ Flight Price Prediction App")
st.write("Enter flight details below and get the predicted price:")

# Input fields
airline = st.selectbox("Airline", ["SpiceJet", "AirAsia", "Vistara", "GO_FIRST", "Indigo", "Air_India"])
source_city = st.selectbox("Source City", ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"])
departure_time = st.selectbox("Departure Time", ["Evening", "Early_Morning", "Morning", "Afternoon", "Night", "Late_Night"])
stops = st.selectbox("Stops", ["zero", "one", "two_or_more"])
arrival_time = st.selectbox("Arrival Time", ["Night", "Morning", "Early_Morning", "Afternoon", "Evening", "Late_Night"])
destination_city = st.selectbox("Destination City", ["Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai", "Delhi"])
travel_class = st.selectbox("Class", ["Economy", "Business"])
duration = st.slider("Duration (hours)", min_value=1.0, max_value=50.0, step=0.1)
days_left = st.slider("Days Left to Travel", min_value=1, max_value=49, step=1)

# Prepare input as DataFrame
input_data = pd.DataFrame({
    "airline": [airline],
    "source_city": [source_city],
    "departure_time": [departure_time],
    "stops": [stops],
    "arrival_time": [arrival_time],
    "destination_city": [destination_city],
    "class": [travel_class],
    "duration": [duration],
    "days_left": [days_left]
})

# Force categorical dtypes with same categories as training
categorical_features = [
    'airline', 'source_city', 'departure_time',
    'arrival_time', 'destination_city', 'stops', 'class'
]

categories_map = {
    "airline": ["SpiceJet", "AirAsia", "Vistara", "GO_FIRST", "Indigo", "Air_India"],
    "source_city": ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"],
    "departure_time": ["Evening", "Early_Morning", "Morning", "Afternoon", "Night", "Late_Night"],
    "stops": ["zero", "one", "two_or_more"],
    "arrival_time": ["Night", "Morning", "Early_Morning", "Afternoon", "Evening", "Late_Night"],
    "destination_city": ["Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai", "Delhi"],
    "class": ["Economy", "Business"]
}

for col in categorical_features:
    input_data[col] = pd.Categorical(input_data[col], categories=categories_map[col])

# Predict button
if st.button("Predict Price 💰"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Flight Price: ₹ {prediction:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
