import streamlit as st
import pickle
import numpy as np

# Load your trained weather model
with open("weather_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌤️ Weather Prediction App")

# Input fields
temperature = st.number_input("Temperature (°C)", value=25.0)
humidity = st.number_input("Humidity (%)", value=60.0)
wind_speed = st.number_input("Wind Speed (km/h)", value=10.0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[temperature, humidity, wind_speed]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Weather Condition: {prediction[0]}")
