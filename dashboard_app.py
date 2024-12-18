import streamlit as st
import json
import os

# File to store user credentials
CREDENTIALS_FILE = "info.json"

# Initialize credentials file if it doesn't exist
if not os.path.exists(CREDENTIALS_FILE):
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump({"admin": "password123"}, file)

# Load user credentials
with open(CREDENTIALS_FILE, "r") as file:
    USER_CREDENTIALS = json.load(file)

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""


# Login function
def login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
    else:
        st.error("Invalid username or password. Please try again.")


# Logout function
def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""


# Signup function
def signup(username, password):
    if username in USER_CREDENTIALS:
        st.error("Username already exists. Please choose a different username.")
    else:
        USER_CREDENTIALS[username] = password
        with open(CREDENTIALS_FILE, "w") as file:
            json.dump(USER_CREDENTIALS, file)
        st.success("Signup successful! You can now log in.")


# Main app
if st.session_state["logged_in"]:
    st.success(f"Welcome, {st.session_state['username']}!")
    st.button("Logout", on_click=logout)
    # Add your application functionality here
    st.markdown(
        """
    <div style="text-align: center;">
        <h2>Dashboard</h2>
    </div>
""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <iframe title="AQI" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiOGExYzY4YzEtMjRhNC00MjAyLTlhZWMtYjRmODcwNjIxNDc1IiwidCI6IjkzZTljMTgyLTdhOWMtNGI4YS04YzY1LTM3OTMyNDZlYzgzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <div style="text-align: left;">
        Prepared by Rajesh Boyina
    </div>
""",
        unsafe_allow_html=True,
    )
else:
    st.title("AIR QUALITY INSIGHTS DASHBOARD")
    st.title("Login / Signup Form")
    choice = st.radio("Select an option:", ["Login", "Signup"])

    if choice == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            login(username, password)

    elif choice == "Signup":
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Signup"):
            if new_password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            elif not new_username or not new_password:
                st.error("Username and password cannot be empty.")
            else:
                signup(new_username, new_password)
