import streamlit as st

# Define user credentials
USER_CREDENTIALS = {"admin": "password123", "user1": "pass1", "user2": "pass2"}

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
        Prepared by Rajesh boyina
    </div>
""",
        unsafe_allow_html=True,
    )
else:
    st.title("AIR QUALITY INSIGHTS DASHBOARD")
    st.title("Login Form")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)
