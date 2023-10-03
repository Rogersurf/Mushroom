# user_mgt_ui.py

import streamlit as st
import Db.dbmgt as db

def app():
    st.subheader("User Management")

    choice = st.radio("Choose action", ["Register", "Display Data", "Update User", "Delete User"])

    if choice == "Register":
        email = st.text_input("Enter your email:")
        mushroom_details = st.text_input("Enter mushroom details:")
        prediction = "edible"  # Replace this with your actual model's prediction when available

        if st.button("Register"):
            try:
                db.register_user(email, mushroom_details, prediction)
                st.success("Registered Successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    elif choice == "Display Data":
        user_data = db.fetch_all_users()
        st.write(user_data)

    elif choice == "Update User":
        email_to_update = st.text_input("Enter the email of the user to update:")
        new_email = st.text_input("Enter the new email:")
        new_mushroom_details = st.text_input("Enter new mushroom details:")

        if st.button("Update"):
            try:
                db.update_user(email_to_update, new_email, new_mushroom_details)
                st.success("Updated Successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    elif choice == "Delete User":
        email_to_delete = st.text_input("Enter the email of the user to delete:")

        if st.button("Delete"):
            try:
                db.delete_user(email_to_delete)
                st.success("Deleted Successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
