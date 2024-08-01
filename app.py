import pandas as pd
import streamlit as st
import pickle
import pandas as pd

#import the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Used Car Price Predictor")

#brand of the car
brand = st.selectbox('Brand', df['brand'].unique())

#model of the car
model = st.selectbox('Model', df['model'].unique())

vehicle_age = st.number_input('Age of vehicle')

km_driven = st.number_input('Number of kms driven')

# seller type
seller_type = st.selectbox('Seller Type', df['seller_type'].unique())

#fuel type
fuel_type = st.selectbox('Fuel type', df['fuel_type'].unique())

#transmission type of the car
transmission_type= st.selectbox('Transmission_type', df['transmission_type'].unique())

mileage = st.number_input('Mileage')

engine = st.number_input('Engine(cc)')

max_power = st.number_input('Maximum power(bhp)')

seats = st.selectbox('Number of seats', [2,4,5,6,7,8,9])

avg_cost_price = st.number_input('Cost Price in INR')

if st.button('Predict Price'):
    data = {'brand': [brand], 'model': [model], 'vehicle_age': [vehicle_age], 'km_driven': [km_driven],
            'seller_type': [seller_type],
            'fuel_type': [fuel_type], 'transmission_type': [transmission_type], 'mileage': [mileage],
            'engine': [engine],
            'max_power': [max_power], 'seats': [seats], 'avg_cost_price': [avg_cost_price]}
    output_df = pd.DataFrame(data)
    ans = pipe.predict(output_df)
    st.title('Predicted Price is ₹ '+ str(int(ans[0])))

