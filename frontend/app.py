# frontend/app.py
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

# Backend API URL - CHANGE this when deploying
API_URL = "http://127.0.0.1:8000"  # Example: https://geoshield-api.herokuapp.com

# Sidebar input
st.sidebar.header("🛠️ GeoShield Input Parameters")
input_data = {
    "rainfall_3day": st.sidebar.slider("🌧️ Rainfall (3-day, mm)", 0, 500, 120),
    "rainfall_15day": st.sidebar.slider("🌧️ Rainfall (15-day, mm)", 0, 1000, 300),
    "ndvi_loss": st.sidebar.slider("🌿 NDVI Loss (0-1)", 0.0, 1.0, 0.35),
    "slope": st.sidebar.slider("⛰️ Slope (degrees)", 0, 90, 35),
    "aspect": st.sidebar.slider("🧭 Aspect (0-360)", 0, 360, 180),
    "proximity_to_road": st.sidebar.slider("🛣️ Distance to Road (km)", 0.0, 5.0, 0.3),
    "proximity_to_landslide": st.sidebar.slider("⚠️ Proximity to Past Landslide (km)", 0.0, 5.0, 0.1),
    "in_lhz_high_risk_zone": st.sidebar.selectbox("🚩 In High-Risk Zone?", [1, 0])
}

# Main page
st.title("🌍 GeoShield Sentinel")
st.subheader("Landslide Vulnerability Forecast Using EO & ML")

# Run prediction button
if st.button("🔍 Run Prediction"):
    with st.spinner("Calling backend API..."):
        # Call /predict endpoint
        response = requests.post(f"{API_URL}/predict", json=input_data)
        result = response.json()
    
    # Show prediction
    st.markdown(f"## 🧭 Prediction: **{'🌋 Landslide Likely' if result['prediction'] == 1 else '✅ No Landslide'}**")
    st.markdown(f"**Probability of Landslide:** {result['probability']:.2%}")
    st.progress(result['probability'])
    
    # Optional: SHAP explainability
    if st.checkbox("Show SHAP Feature Contribution"):
        with st.spinner("Calling backend for SHAP explanation..."):
            explain_response = requests.post(f"{API_URL}/explain", json=input_data)
            explain_result = explain_response.json()
            
        # Display SHAP values as simple bar chart
        fig, ax = plt.subplots()
        features = explain_result["features"]
        shap_values = explain_result["shap_values"]
        
        ax.barh(features, shap_values)
        ax.set_title("Feature Contribution (SHAP)")
        st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Built using Streamlit • FastAPI • CHIRPS • Sentinel-2 • CartoDEM • SHAP • RandomForest")