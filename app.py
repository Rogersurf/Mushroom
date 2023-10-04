import streamlit as st
import importlib


# Use importlib to load your pages
home = importlib.import_module("pages.1_🏠_Home")
regression = importlib.import_module("pages.2_🍄_Edible_or_Poisoning")
recommender = importlib.import_module("pages.3_🔍_Mushroom_recommendation")
eda_ui = importlib.import_module("pages.4_📊_Exploratory_Data_Analysis")
user_mgt_ui = importlib.import_module("pages.5_👥_User_Management")

st.set_page_config(page_title="🍄Mushroom Dashboard App 📊", layout="wide", initial_sidebar_state="expanded")

# Page functions dictionary
page_dict = {
    "🏠 Home": home.app,
    "🍄 Edible or Poisoning?": regression.app,
    "🔍 Mushroom recommendation": recommender.app,
    "📊 Exploratory Data Analysis": eda_ui.app,
    "👥 User Management": user_mgt_ui.app
}

# Main function for the app
def main():
    # Main Content Area
    if 'page' not in st.session_state:
        st.session_state.page = "🏠 Home"

    # Run the corresponding app function
    page_function = page_dict[st.session_state.page]
    page_function()

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