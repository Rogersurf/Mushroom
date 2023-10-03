import streamlit as st

def app():
    # Container for the Title
    with st.container():      
        # Displaying the image
        st.image("G:\My Drive\Colab Notebooks\Mushroom\Data\Images\mushroom menu.jpg", use_column_width=True)  # use_column_width resizes the image to the column width
        
        # Container for some description or introduction
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
        
        # Optionally, you can add more containers with more information or images.
        st.markdown("""
        ## 📊 Quick Stats 📊
        - **Total Mushrooms:** 5000
        - **Edible Mushrooms:** 3000
        - **Poisonous Mushrooms:** 2000
        - **Most Common Mushroom:** XYZ
        """)
        
        # You can add more visual elements like charts, plots, etc.
        st.bar_chart({'Edible': [3000], 'Poisonous': [2000]})
        
        # Adding a footer
        st.markdown("""
        ---
        ###### Developed by [Roger Braun©](www.linkedin.com/roger-braun) 🚀
        """) # Replace with the correct path to your image