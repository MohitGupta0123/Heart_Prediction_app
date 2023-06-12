import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# Load the trained ML model
model = pickle.load(open("heart_disease_prediction.pkl", "rb"))

# Define the function to predict heart disease
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Create a DataFrame with the input values
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                              columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"])
    # Make the prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Set pink background color
page_bg_img = '''
<style>
body {
background-image: url("https://cdn.pixabay.com/photo/2018/04/24/07/48/pink-3345632_960_720.png");
background-size: cover;
}
</style>
'''

# Create a Streamlit web app
def main():
    # Set the app title and background color
    st.title("Heart Disease Prediction")
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Create input fields for user to enter the 13 numerical inputs
    age = st.number_input("Age", min_value=1, max_value=100)
    sex = st.selectbox("Sex", [0, 1])
    cp = st.selectbox("Chest Pain Type", [1, 2, 3, 4])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=1, max_value=250)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=1, max_value=600)
    fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
    restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=1, max_value=250)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", [1, 2, 3])
    ca = st.number_input("Number of Major Vessels", min_value=0, max_value=3)
    thal = st.number_input("Thalassemia", min_value=1, max_value=7)

    # Check if the user has entered all the inputs
    if st.button("Predict"):
        if None not in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
            # Make the prediction
            prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
            if prediction == 1:
                st.write("Prediction: You have heart disease.")
            else:
                st.write("Prediction: You do not have heart disease.")
        else:
            st.write("Please enter all the inputs.")

# Run the app
if __name__ == "__main__":
    main()
