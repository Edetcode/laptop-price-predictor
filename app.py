import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("laptop_price_model.joblib")

st.title("💻 Laptop Price Predictor")
st.write("Select laptop specifications to estimate its price (€).")

# --- User Inputs ---
company = st.selectbox("Brand", ["Dell", "HP", "Lenovo", "Apple", "Asus", "Acer", "MSI", "Toshiba", "Samsung", "Other"])
typename = st.selectbox("Type", ["Notebook", "Ultrabook", "Gaming", "Workstation", "2 in 1 Convertible", "Netbook"])
cpu = st.selectbox("CPU", ["Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
                           "AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1", "Apple M2"])
ram_gb = st.selectbox("RAM (GB)", [4, 8, 16, 32, 64])
memory_gb = st.selectbox("Storage (GB)", [128, 256, 512, 1024, 2048])
memory_type = st.selectbox("Storage Type", ["SSD", "HDD", "Hybrid", "Flash"])
gpu_brand = st.selectbox("GPU Brand", ["Intel", "Nvidia", "AMD", "Apple"])
gpu_type = st.selectbox("GPU Type", ["Integrated", "Dedicated"])
opsys = st.selectbox("Operating System", ["Windows", "MacOS", "Linux", "No OS", "Chrome OS"])
inches = st.selectbox("Screen Size (inches)", [11.6, 13.3, 14.0, 15.6, 17.3])
screenresolution = st.selectbox("Screen Resolution", ["1366x768", "1920x1080", "2560x1440", "3840x2160"])
weight = st.selectbox("Weight (kg)", [1.0, 1.2, 1.5, 2.0, 2.5, 3.0])

# --- Encoding categorical values into numbers ---
def encode_value(val, mapping):
    return mapping.get(val, -1)  # -1 for unknowns

company_map = {c: i for i, c in enumerate(["Dell", "HP", "Lenovo", "Apple", "Asus", "Acer", "MSI", "Toshiba", "Samsung", "Other"])}
typename_map = {c: i for i, c in enumerate(["Notebook", "Ultrabook", "Gaming", "Workstation", "2 in 1 Convertible", "Netbook"])}
cpu_map = {c: i for i, c in enumerate(["Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
                                       "AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1", "Apple M2"])}
memory_type_map = {c: i for i, c in enumerate(["SSD", "HDD", "Hybrid", "Flash"])}
gpu_brand_map = {c: i for i, c in enumerate(["Intel", "Nvidia", "AMD", "Apple"])}
gpu_type_map = {"Integrated": 0, "Dedicated": 1}
opsys_map = {c: i for i, c in enumerate(["Windows", "MacOS", "Linux", "No OS", "Chrome OS"])}
screen_map = {c: i for i, c in enumerate(["1366x768", "1920x1080", "2560x1440", "3840x2160"])}

# --- Build full numeric feature set ---
user_input = pd.DataFrame([{
    "company": encode_value(company, company_map),
    "typename": encode_value(typename, typename_map),
    "cpu": encode_value(cpu, cpu_map),
    "ram_gb": ram_gb,
    "ram": ram_gb,
    "memory_gb": memory_gb,
    "memory_type": encode_value(memory_type, memory_type_map),
    "memory": memory_gb,
    "gpu_brand": encode_value(gpu_brand, gpu_brand_map),
    "gpu_type": encode_value(gpu_type, gpu_type_map),
    "gpu": encode_value(gpu_brand, gpu_brand_map),  # simplified
    "gpu_is_dedicated": 1 if gpu_type == "Dedicated" else 0,
    "opsys": encode_value(opsys, opsys_map),
    "os_type": encode_value(opsys, opsys_map),
    "inches": inches,
    "screenresolution": encode_value(screenresolution, screen_map),
    "weight": weight,
    "is_windows": 1 if "Windows" in opsys else 0,
    "is_macos": 1 if "MacOS" in opsys else 0,
    "has_hdd": 1 if memory_type == "HDD" else 0,
    "has_ssd": 1 if memory_type == "SSD" else 0,
    "has_flash_storage": 1 if memory_type == "Flash" else 0,
    "screen_size_category": 1,  # placeholder numeric
    "weight_category": 1,
    "is_touchscreen": 0,
    "screen_type": 1,
    "product": 1,
    "product_line": 1,
    "laptop_id": 0,
    "is_premium_brand": 1 if company in ["Apple", "MSI"] else 0,
    "resolution_width": 1920,
    "resolution_height": 1080,
    "resolution_pixels": 1920 * 1080,
    "cpu_brand": 0 if "Intel" in cpu else (1 if "AMD" in cpu else 2),
    "cpu_type": 1,
    "cpu_generation": 10,
    "cpu_speed_ghz": 2.5,
    "cpu_performance_score": 1000,
    "ram_memory_interaction": ram_gb * memory_gb,
    "screen_size_weight_ratio": round(inches / weight, 2),
}])

# --- Predict ---
if st.button("Predict Price"):
    try:
        prediction = model.predict(user_input)[0]
        st.success(f"💰 Estimated Laptop Price: €{prediction:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
