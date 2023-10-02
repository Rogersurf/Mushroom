import streamlit as st
from pages import home, recommender, regression, eda_ui

st.set_page_config(page_title="🍄Mushroom Dashboard App 📊", layout="wide")

PAGES = {
    "Home": home,
    "Edible or Poisoning?": regression,
    "Mushroom recommendation": recommender,
    "EDA": eda_ui
}

# Main app
def main():
    container = st.container()

    with container:
        st.markdown("<h1 style='text-align: center; color: blue;'>Welcome to Mushroom Dashboard</h1>", unsafe_allow_html=True)

        cols = st.columns(4)

        with cols[0]:
            if st.button("Go to Home"):
                home.app()

        with cols[1]:
            if st.button("Edible or Poisoning?"):
                regression.app()

        with cols[2]:
            if st.button("Mushroom recommendation"):
                recommender.app()

        with cols[3]:
            if st.button("EDA"):
                eda_ui.app()

# Run the app
if __name__ == "__main__":
    main()