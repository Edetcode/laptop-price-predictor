import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("laptop_price_model.joblib")

st.title("💻 Laptop Price Predictor")
st.write("Select laptop specifications to estimate its price (€).")

# --- Dropdown Inputs ---
company = st.selectbox("Brand", ["Dell", "HP", "Lenovo", "Apple", "Asus", "Acer", "MSI", "Toshiba", "Samsung", "Other"])
type_name = st.selectbox("Type", ["Notebook", "Ultrabook", "Gaming", "Workstation", "2 in 1 Convertible", "Netbook"])
cpu_brand = st.selectbox("CPU Brand", ["Intel", "AMD", "Apple M1/M2"])
cpu_type = st.selectbox("CPU Type", ["i3", "i5", "i7", "i9", "Ryzen 3", "Ryzen 5", "Ryzen 7", "M1", "M2"])
ram_gb = st.selectbox("RAM (GB)", [4, 8, 16, 32, 64])
memory_gb = st.selectbox("Storage (GB)", [128, 256, 512, 1024, 2048])
gpu_brand = st.selectbox("GPU Brand", ["Intel", "Nvidia", "AMD", "Apple"])
os = st.selectbox("Operating System", ["Windows", "MacOS", "Linux", "No OS", "Chrome OS"])
screen_size = st.selectbox("Screen Size (inches)", [11.6, 13.3, 14.0, 15.6, 17.3])
resolution = st.selectbox("Resolution", ["1366x768", "1920x1080", "2560x1440", "3840x2160"])
weight = st.selectbox("Weight (kg)", [1.0, 1.2, 1.5, 2.0, 2.5, 3.0])

# --- Convert Inputs to DataFrame ---
user_input = pd.DataFrame([{
    "company": company,
    "type_name": type_name,
    "cpu_brand": cpu_brand,
    "cpu_type": cpu_type,
    "ram_gb": ram_gb,
    "memory_gb": memory_gb,
    "gpu_brand": gpu_brand,
    "os": os,
    "screen_size": screen_size,
    "resolution": resolution,
    "weight": weight
}])

# --- Predict Button ---
if st.button("Predict Price"):
    try:
        prediction = model.predict(user_input)[0]
        st.success(f"💰 Estimated Laptop Price: €{prediction:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
