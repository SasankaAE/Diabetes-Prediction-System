import streamlit as st
import pickle

model = pickle.load(open("diabetes-predict-model.pkl", "rb"))

st.title("Diabetes Prediction System")

glucose = st.number_input("Glucose Level")
bmi = st.number_input("BMI")

if st.button("Predict"):
    result = model.predict([[glucose, bmi]])

    if result[0] == 1:
        st.error("Diabetic")
    else:
        st.success("Non-Diabetic")