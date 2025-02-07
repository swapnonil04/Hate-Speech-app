import streamlit as st
import pickle

# Load the trained model
with open('hatespeech_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Swapss Hate Speech Detection App")

# Input text from the user
user_input = st.text_area("Enter text to analyze:")

if st.button("Detect Hate Speech"):
    prediction = model.predict([user_input])
    if prediction[0] == 1:
        result="Hate Speech Detected"
    else:
        result="No Hate Speech Detected"
    st.write(f"Prediction: {result}")
