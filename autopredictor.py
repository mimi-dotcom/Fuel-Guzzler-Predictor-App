

import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Fuel Guzzler Predictor")
pickle_in = open('mpg.pkl', 'rb')
model = pickle.load(pickle_in)

No_cylinders = st.number_input("No of cylinders in the car")
displacement = st.number_input("whats the engine cc ?")
horsepower = st.number_input("Enter the Horsepower")
weight = st.number_input("weight of the car in kg")
acceleration = st.number_input("how long does it take from 0-60mph in seconds")
modelyear = st.number_input("Enter the year of manufacture")

origin_country = st.selectbox("select the country of origin", [
                              'American', 'European', 'Asian'])

if(origin_country == 'American'):
    origin = 1
elif(origin_country == 'European'):
    origin = 2
elif(origin_country == 'Asian'):
    origin = 3

mileage = model.predict([[No_cylinders, displacement, horsepower, weight,
                        acceleration, modelyear, origin]])

st.title(f"""Mileage of the car is""")
st.title(f"""{round(mileage[0],2)}kilometers per litre""")


st.write(" ")
st.write(" ")
