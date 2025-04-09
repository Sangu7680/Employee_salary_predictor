import streamlit as st
import pandas as pd
import pickle  # or joblib

# Load the trained model
with open('salary_model.pkl', 'rb') as file:
    model = pickle.load(file)


# Set the title of the app
st.title('IT-Salary Prediction of App')

# Create input fields for user input
experience = st.number_input('Years of Experience:', min_value=1)
Age=st.number_input("Your Age:",min_value=18)
education_level = st.selectbox('Education Level:', ['High School', 'Bachelor', 'Master', 'PhD'])
job_title = st.selectbox('Job Title:', ['Manager', 'Director', 'Analyst', 'Engineer'])

# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'Experience': [experience],
    "Age":[Age],
    'Education_Bachelor': [1 if education_level == 'Bachelor' else 0],
    'Education_High School': [1 if education_level == 'High School' else 0],
    'Education_Master': [1 if education_level == 'Master' else 0],
    'Education_PhD': [1 if education_level == 'PhD' else 0],
    'Job_Title_Analyst': [1 if job_title == 'Analyst' else 0],
    'Job_Title_Director': [1 if job_title == 'Director' else 0],
    'Job_Title_Engineer': [1 if job_title == 'Engineer' else 0],
    'Job_Title_Manager': [1 if job_title == 'Manager' else 0],
})

# Make predictions when the button is pressed
if st.button('Predict Salary'):
    prediction = model.predict(input_data)
    st.success(f'Predicted Salary: ₹{prediction[0]:,.2f} RUPEES')
