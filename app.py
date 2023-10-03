import sys
sys.path.append("G:/My Drive/Colab Notebooks/Mushroom")
import streamlit as st
from pages import home, recommender, regression, eda_ui, user_mgt_ui

st.set_page_config(page_title="🍄Mushroom Dashboard App 📊", layout="wide")

# Add CSS to keep sidebar always open
st.markdown("""
    <style>
        .reportview-container .main .block-container {
            max-width: 100%;
        }
        div[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 100%;
            max-width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

# Main function for the app
def main():

    # Sidebar without page filename
    st.sidebar.markdown("<h1 style='text-align: center; color: blue;'>Mushroom Dashboard</h1>", unsafe_allow_html=True)

    if st.sidebar.button("🏠 Home"):
        st.session_state.page = "Home"
    
    if st.sidebar.button("🍄 Edible or Poisoning?"):
        st.session_state.page = "Edibility"

    if st.sidebar.button("🔍 Mushroom recommendation"):
        st.session_state.page = "Recommendation"

    if st.sidebar.button("📊 Exploratory Data Analysis"):
        st.session_state.page = "EDA"

    if st.sidebar.button("👥 User Management"):
        st.session_state.page = "User Management"

    # Main Content Area
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    if st.session_state.page == "Home":
        home.app()
    elif st.session_state.page == "Edibility":
        regression.app()
    elif st.session_state.page == "Recommendation":
        recommender.app()
    elif st.session_state.page == "EDA":
        eda_ui.app()
    elif st.session_state.page == "User Management":
        user_mgt_ui.app()

    # Footer
    st.markdown("---")
    st.markdown("""
    <p style='text-align: center;'>
    🍄 Mushroom Dash © 2023 | Created by <a href="https://www.linkedin.com/in/roger-braun" target="_blank">Roger Braun</a>
    </p>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()