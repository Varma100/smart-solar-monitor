import streamlit as st
import pandas as pd
import pickle
import altair as alt

# Load data
df = pd.read_csv("solar_data.csv")

# Load model
with open("solar_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Smart Solar Energy Monitor", layout="wide")
st.title("🔆 Smart Solar Energy Monitor")

# 📋 Show column names for debugging
st.write("📋 Columns in your data:")
st.write(df.columns.tolist())

# 📄 Raw Data Table
st.subheader("📄 Raw Solar Data")
st.dataframe(df.head())

# 📈 Line Chart: Power Output vs Irradiance
st.subheader("📈 Power Output vs Irradiance")
st.line_chart(df[["Irradiance", "Power_Output"]])

# 🧪 Scatter Plot with Tooltips
st.subheader("🧪 Irradiance vs Power Output (Interactive)")
chart = alt.Chart(df).mark_circle(size=60).encode(
    x="Irradiance",
    y="Power_Output",
    tooltip=["Temperature", "Humidity", "Irradiance", "Power_Output"]
).interactive()
st.altair_chart(chart, use_container_width=True)

# 🔮 Prediction Tool
# 🔮 Prediction Tool (Updated for 3 features)
st.subheader("🔮 Predict Power Output")

# Input sliders for each feature
temp = st.slider("Temperature (°C)", 0, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 50)
irradiance = st.slider("Irradiance (W/m²)", 0, 1200, 600)

# Predict when button is clicked
if st.button("Predict Power Output"):
    input_data = [[temp, humidity, irradiance]]  # Match model input shape
    prediction = model.predict(input_data)
    st.success(f"Estimated Output: {prediction[0]:.2f} kWh")

