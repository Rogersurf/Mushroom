# Import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


# Set Page Config
st.set_page_config(
    page_title="Final Assignment - Roger Braun",
    page_icon="✅",
    layout="wide",
)

# Load Data
@st.cache_data
def load_data():
    # Define the file path
    filename = "G:\My Drive\Colab Notebooks\Mushroom\mushrooms_dataset.csv"

    # Load your data here
    df = pd.read_csv(filename)
    return df

df = load_data()

# Title and Description
st.title("Mushroom Dataset Project")

# Sidebar: Filters and Options
st.sidebar.header("Filters and Options")

st.markdown("""
            This dashboard showcases some of the factors that are related to sustainability and environmental performance measures across different countries worldwide. The dashboard takes different sustainability variables and components to analyse the continents and the countries’ position in a sustainable lifestyle.
""")
with st.expander("📊 **Key Components of the Analysis**"):
                 st.markdown("""
                The key components are necessary variables that can help answer the question of which continents and countries have sustainable energy approaches.
                 - Years: An interval of time.
                 - Continent: Which continent are present in the dataframe?
                 - Access to clean fuels for cooking: Is this still a worldwide problem?
                 - Renewables % equivalent primary energy: How much of the energy is renewable?
                 - Renewable-electricity-generating-capacity-per-capita: A more accurate measure for the differences in sizes of the continents and countries?
"""
)


# Add your filters and options here, like sliders, selectbox, multiselect etc.
# Sidebar filter: Features
features = df.columns.tolist()
selected_features = st.sidebar.multiselect("Select Features 🌍", features, default=features)
if not selected_features:
    st.warning("Please select a feature from the side bar ⚠️")
    st.stop()
filtered_df = df[df[selected_features].isin(selected_features)]

selected_features = st.multiselect(
        'Select Features', options=df.columns.tolist(), default=df.columns.tolist()
        )


# Main: Data and Visualizations
# You can add different sections or components for different visualizations or insights.

# Dropdown to select the type of visualization
visualization_option = st.selectbox(
    "Select Visualization 🎨", 
    ["Box plot of Wordwide Renewable Electricity Generating Capacity Per Capity By Year",
    "Heatmap of Average Access to Clean Cooking Fuels by Continent and Year", 
    "Are renewables for the rich? (Scatterplot for each individual country)",
    "Scatterplot of GDP Growth vs. share of renewable energy by Continent"])

# Visualizations based on user selection
if visualization_option == "Box plot of Wordwide Renewable Electricity Generating Capacity Per Capity By Year":
# Boxplot for renewable electricity
# Display the average values
    
# Create a barchart
    plt.figure()
    st.pyplot(plt)

elif visualization_option == "Heatmap of Average Access to Clean Cooking Fuels by Continent and Year":
    plt.figure()
    st.pyplot(plt)

elif visualization_option == "Are renewables for the rich? (Scatterplot for each individual country)":
    plt.figure()
    st.pyplot(plt)

elif visualization_option == "Scatterplot of GDP Growth vs. share of renewable energy by Continent":
    plt.figure()
    st.pyplot(plt)

# Insights from Visualization Section
with st.expander("Insights from Visualization"):
    st.markdown("""
    Write your insights here.
    """)

# Display dataset overview or any other information you want.
st.header("Dataset Overview")
# Your code to display dataset overview or any other information.
# Display dataset overview
st.header("Dataset Overview")
st.dataframe(df.describe())