import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import numpy as np
from pathlib import Path

BASE_PATH = Path("./Data/Models")

def load_data():
    data = {
        'username': ['user1', 'user1', 'user2', 'user3', 'user3'],
        'item': ['item1', 'item2', 'item2', 'item3', 'item1'],
        'rating': [5, 4, 3, 5, 2]
    }
    return pd.DataFrame(data)

def create_interaction_matrix(df, user_col, item_col, rating_col, threshold=0):
    interactions = df.groupby([user_col, item_col])[rating_col] \
        .sum().unstack().reset_index().fillna(0).set_index(user_col)
    interactions = interactions.applymap(lambda x: 1 if x > threshold else 0)
    return interactions

def get_username_encoder(df):
    le_username = LabelEncoder()
    df['username_encoded'] = le_username.fit_transform(df['username'])
    return le_username

def reduce_dimensionality(interaction_matrix):
    n_components = min(interaction_matrix.shape[1] - 1, 50)
    svd = TruncatedSVD(n_components=n_components)
    reduced_matrix = svd.fit_transform(interaction_matrix)
    return svd, reduced_matrix

def get_recommendations(username, le_username, reduced_matrix):
    if username in le_username.classes_:
        user_id = le_username.transform([username])[0]
        user_ratings = reduced_matrix[user_id]
        similarity_scores = cosine_similarity([user_ratings], reduced_matrix)[0]
        similar_items = np.argsort(similarity_scores)[-6:-1][::-1]
        return similar_items
    else:
        return []

def save_models(le_username, svd, reduced_matrix):
    joblib.dump(le_username, BASE_PATH / 'le_username.pkl')
    joblib.dump(svd, BASE_PATH / 'svd_model.pkl')
    joblib.dump(reduced_matrix, BASE_PATH / 'reduced_matrix.pkl')

def load_models():
    le_username = joblib.load(BASE_PATH / 'le_username.pkl')
    svd = joblib.load(BASE_PATH / 'svd_model.pkl')
    reduced_matrix = joblib.load(BASE_PATH / 'reduced_matrix.pkl')
    return le_username, svd, reduced_matrix

def app():
    df = load_data()
    interaction_matrix = create_interaction_matrix(df, 'username', 'item', 'rating', threshold=3)
    le_username = get_username_encoder(df)
    svd, reduced_matrix = reduce_dimensionality(interaction_matrix)
    save_models(le_username, svd, reduced_matrix)

if __name__ == "__main__":
    app()