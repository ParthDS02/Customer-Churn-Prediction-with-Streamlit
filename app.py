import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Insights: Churn Prediction App")

st.divider()

st.write("Enter the required values and click on the 'Predict' button to generate your prediction.")

st.divider()

age = st.number_input("Enter Age", min_value = 10, max_value = 100, value = 30)

tenure = st.number_input("Enter Tenure", min_value= 0, max_value = 130, value = 10)

monthlycharege = st.number_input("Enter Monthly Charege", min_value = 30, max_value = 150)

gender = st.selectbox("Select your Gender", ["Male", "Female"])

# Clear Inputs button
if st.button("Clear Output"):
    st.experimental_rerun()

st.divider()

predictbutton = st.button("Predict!")

st.divider()

if predictbutton:

    gender_selected = 1 if gender == "Female" else 0

    x= [age, gender_selected, tenure, monthlycharege]

    x1 = np.array(x)

    x_array = scaler.transform([x1])

    prediction = model.predict(x_array)[0]

    predicted = "Yes" if prediction == 1 else "No"

    st.balloons()

    st.write (f" Predicted: {predicted}")

else:
    st.write("Note : If the result is not generated or an error occurs, please enter the value again and click the 'Predict' button.")
