import sys
sys.path.append("G:/My Drive/Colab Notebooks/Mushroom")
import streamlit as st
from pages import home, recommender, regression, eda_ui, user_mgt_ui  # <-- Include new page here

st.set_page_config(page_title="🍄Mushroom Dashboard App 📊", layout="wide")

PAGES = {
    "Home": home,
    "Edible or Poisoning?": regression,
    "Mushroom recommendation": recommender,
    "EDA": eda_ui,
    "User Management": user_mgt_ui  # <-- Add new page to the dict
}

def main():
    container = st.container()

    with container:
        st.markdown("<h1 style='text-align: center; color: blue;'>Welcome to Mushroom Dashboard</h1>", unsafe_allow_html=True)

        cols = st.columns(5)  # Five columns to accommodate all the pages

        with cols[0]:
            st.markdown("🏠 **Home**", unsafe_allow_html=True)  # Added icons and descriptions
            if st.button("Go to Home"):
                home.app()

        with cols[1]:
            st.markdown("🍄 **Edibility Check**", unsafe_allow_html=True)  # You can change the icons as per your liking
            if st.button("Edible or Poisoning?"):
                regression.app()

        with cols[2]:
            st.markdown("🔍 **Mushroom Recommendation**", unsafe_allow_html=True)
            if st.button("Mushroom recommendation"):
                recommender.app()

        with cols[3]:
            st.markdown("📊 **Exploratory Data Analysis**", unsafe_allow_html=True)
            if st.button("EDA"):
                eda_ui.app()

        with cols[4]: 
            st.markdown("👥 **User Management**", unsafe_allow_html=True)
            if st.button("User Management"):
                user_mgt_ui.app()

    # Footer for the app
    st.markdown("---")  # This adds a line for separation
    st.markdown("""
    <p style='text-align: center;'>
    🍄 Mushroom Dash © 2023 | Created by <a href="https://www.linkedin.com/in/roger-braun" target="_blank">Roger Braun</a>
    </p>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()