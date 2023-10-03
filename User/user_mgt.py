# user_management.py
import streamlit as st
import Db.dbmgt as db

def user_mgt():
    st.subheader("User Management")

    choice = st.radio("Choose action", ["Register", "Display Data", "Update Information", "Delete Record"])

    if choice == "Register":
        email = st.text_input("Enter your email:")
        mushroom_details = st.text_input("Enter mushroom details:")
        
        # Predict the edibility of the mushroom here
        prediction = "edible"  # placeholder, replace with your model's prediction

        if st.button("Register"):
            db.register_user(email, mushroom_details, prediction)
            st.success("Registered Successfully!")

    elif choice == "Display Data":
        user_data = db.fetch_all_users()
        st.write(user_data)

    elif choice == "Update Information":
        email_to_update = st.text_input("Enter the email of the record you want to update:")
        new_email = st.text_input("Enter the new email (or leave blank to keep unchanged):")
        new_mushroom_details = st.text_input("Enter the new mushroom details (or leave blank to keep unchanged):")
    
    if st.button("Update"):
        try:
            db.update_user(email_to_update, new_email, new_mushroom_details)
            st.success("Information Updated Successfully!")
        except ValueError as e:
            st.error(e)

    elif choice == "Delete Record":
        email_to_delete = st.text_input("Enter the email of the record you want to delete:")
    
    if st.button("Delete"):
        try:
            db.delete_user(email_to_delete)
            st.success("Record Deleted Successfully!")
        except ValueError as e:
            st.error(e)

