import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load('car_price_model.pkl')

st.set_page_config(page_title='🚗 Car Price Predictor', layout='centered')
st.title('🚗 Used Car Price Prediction App')

year = st.number_input("Year of Purchase", min_value=1990, max_value=2024, value=2015)
present_price = st.number_input("Present Showroom Price (in Lakh)", min_value=0.0, step=0.1)
kms_driven = st.number_input("KMs Driven", min_value=0)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual'])
transmission = st.selectbox("Transmission Type", ['Manual', 'Automatic'])

# Encoding maps
fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
seller_map = {'Dealer': 0, 'Individual': 1}
trans_map = {'Manual': 0, 'Automatic': 1}

if st.button('Predict Price'):
    input_data = np.array([[present_price, kms_driven, owner,
                            fuel_map[fuel_type],
                            seller_map[seller_type],
                            trans_map[transmission],
                            year]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Resale Price: ₹{round(prediction, 2)} Lakh")
