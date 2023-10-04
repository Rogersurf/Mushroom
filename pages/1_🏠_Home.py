import streamlit as st
from pathlib import Path
import importlib

from Db import db_user_content

recommender = importlib.import_module("pages.3_🔍_Mushroom_recommendation")


BASE_PATH = Path("./Data/Models")

def load():
    le_username, svd, reduced_matrix = db_user_content.load_models()
    return le_username, svd, reduced_matrix

def app():
    with st.container():
        st.image("./Data/Images/mushroom menu.jpg", use_column_width=True)

        le_username, svd, reduced_matrix = load()
        user_input = st.text_input("Enter your username:", placeholder="e.g. user123")

    if user_input:
        try:
            top5 = db_user_content.get_top_recommendations(user_input)

            if top5:
                st.markdown("### Top 5 Mushroom Recommendations for You")
                for mushroom in top5:
                    st.write(mushroom)
            else:
                st.write("No recommendations available for the given username.")
        except Exception as e:
            st.write("Oops! Something went wrong. Please try again.")
            st.write(f"Error: {e}")

    st.markdown("""
    ## 🍄 Welcome to the Mushroom Dashboard 🍄
    This dashboard provides insights, analytics, and predictions related to mushrooms.
    Explore the various sections to uncover patterns, understand relationships, and make informed decisions.
    
    - **Explore:** Dive deep into the data and observe the trends and patterns.
    - **Predict:** Utilize machine learning models to predict whether a mushroom is edible or poisonous.
    - **Recommend:** Get recommendations for mushrooms based on certain characteristics.
    - **Analyze:** Conduct in-depth analysis to derive meaningful insights from the data.
    
    Enjoy exploring the mysterious world of mushrooms! 🌍
    """)

    st.markdown("""
    ## 📊 Quick Stats 📊
    - **Total Mushrooms:** 5000
    - **Edible Mushrooms:** 3000
    - **Poisonous Mushrooms:** 2000
    - **Most Common Mushroom:** XYZ
    """)

    st.bar_chart({'Edible': [3000], 'Poisonous': [2000]})
    
    st.markdown("""
    ---
    ###### Developed by [Roger Braun©](www.linkedin.com/roger-braun) 🚀
    """)

if __name__ == "__main__":
    app()
