import streamlit as st

# Dummy user database
users = {
    "admin": "admin123",
    "user": "user123"
}

def login(username, password):
    return users.get(username) == password

def main():
    st.set_page_config(page_title="Login Page", layout="centered")

    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if login(username, password):
            st.success(f"Welcome, {username}!")
            st.balloons()
            # Place the main app here after login
            st.write("You can now access the application.")
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()
