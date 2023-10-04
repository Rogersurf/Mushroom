import streamlit as st
import pandas as pd
from joblib import load
from sklearn.tree import DecisionTreeClassifier
import pickle


# Define base path
base_path = 'G:/My Drive/Colab Notebooks/Mushroom/'

# Load the model using pickle and base_path
with open(base_path + 'Data/Models/Tree/dt_model.pkl', 'rb') as f:
    best_dt = pickle.load(f)

def preprocess_input(input_data):
    # Process the input data to match the format your model expects
    # This might include encoding, normalization, etc.
    # For simplicity, let's assume the data is already in the correct format
    processed_data = input_data
    return processed_data

def app():
    st.title("Mushroom Edibility Predictor")

    # Display saved data
    data = pd.read_csv('path_to_saved_data.csv')
    st.write(data)

    # User input
    # Let's assume you have two features for simplicity: cap_shape and cap_color
    cap_shape = st.selectbox('Select Cap Shape', ['bell', 'conical', 'convex', 'flat', 'knobbed', 'sunken'])
    cap_color = st.selectbox('Select Cap Color', ['brown', 'yellow', 'white', 'gray', 'red', 'pink', 'buff', 'purple', 'cinnamon', 'green'])

    # Preprocess input
    input_data = pd.DataFrame([[cap_shape, cap_color]], columns=['cap_shape', 'cap_color'])
    processed_data = preprocess_input(input_data)

    # Model prediction
    if st.button("Predict"):
        prediction = best_dt.predict(processed_data)
        if prediction[0] == 1:  # Assuming 1 means edible and 0 means not
            st.success("The mushroom is edible!")
        else:
            st.error("The mushroom is poisonous!")

if __name__ == '__main__':
    app()