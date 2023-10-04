import streamlit as st
import pandas as pd
from joblib import load
from sklearn.tree import DecisionTreeClassifier
import pickle
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
import numpy as np


# Define base path
BASE_PATH = "G:\\My Drive\\Colab Notebooks\\Mushroom\\"

FEATURE_COLUMNS = [
    "cap-shape", "cap-surface", "cap-color", "bruises", "odor", "gill-attachment",
    "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root",
    "stalk-surface-above-ring", "stalk-surface-below-ring", "stalk-color-above-ring",
    "stalk-color-below-ring", "veil-type", "veil-color", "ring-number", "ring-type",
    "spore-print-color", "population", "habitat"
]

class_map = {'e': 'edible', 'p': 'poisonous'}

# Load the model and encoder
with open(BASE_PATH + 'Data/Models/Tree/dt_model.pkl', 'rb') as f:
    best_dt = pickle.load(f)

with open(BASE_PATH + 'Data/Models/Tree/encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

with open(BASE_PATH + 'Data/Models/Tree/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open(BASE_PATH + 'Data/Models/Tree/pca_model.pkl', 'rb') as f:
    pca_model = pickle.load(f)

with open(BASE_PATH + 'Data/Models/Tree/kmeans_model.pkl', 'rb') as f:  # Assuming you've saved the KMeans model with this name
    kmeans = pickle.load(f)

def preprocess_input(input_data):
    # One-hot encode the data using the saved encoder
    encoded_data = encoder.transform(input_data)

    # Scaling the data using the saved scaler
    scl_data = scaler.transform(encoded_data)
    
    # Apply PCA transformation
    pca_transformed_data = pca_model.transform(scl_data)
    
    # Convert PCA-transformed data to DataFrame
    pca_transformed_df = pd.DataFrame(data=pca_transformed_data, columns=['PC1', 'PC2'])

    # Assigning cluster labels
    pca_transformed_df['cluster'] = kmeans.predict(scl_data)
    
    return pca_transformed_df


def app():
    st.title("Mushroom Edibility Predictor")

    input_data = {
    'cap-shape': 'convex',
    'cap-surface': 'scaly',
    'cap-color': 'brown',
    'bruises': 'bruises',
    'odor': 'pungent',
    'gill-attachment': 'free',
    'gill-spacing': 'close',
    'gill-size': 'narrow',
    'gill-color': 'black',
    'stalk-shape': 'enlarging',
    'stalk-root': 'equal',
    'stalk-surface-above-ring': 'smooth',
    'stalk-surface-below-ring': 'smooth',
    'stalk-color-above-ring': 'white',
    'stalk-color-below-ring': 'white',
    'veil-type': 'partial',
    'veil-color': 'white',
    'ring-number': 'one',
    'ring-type': 'pendant',
    'spore-print-color': 'black',
    'population': 'scattered',
    'habitat': 'woods'
}

    # Convert input_data_dict to DataFrame
    input_data_df = pd.DataFrame([input_data])
    # Display input data
    st.write(input_data_df)
    input_data_df = input_data_df.reset_index(drop=True)

    # Preprocess the input data
    processed_data = preprocess_input(input_data_df)
    print(processed_data.shape)

    # Model prediction
    if st.button("Predict"):
        prediction = best_dt.predict(processed_data)
        st.write(prediction)
    
        # Checking the first element of the prediction array
        # Assuming the prediction is for a single input and you want the first result
        if prediction[0] == 'e':
            st.success("The mushroom is edible!")
        else:
            st.error("The mushroom is poisonous!")


        

if __name__ == '__main__':
    app()