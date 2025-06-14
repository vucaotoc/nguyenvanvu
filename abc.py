import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")

# --- CSS Styling ---
page_bg = """
<style>
body {
    background-color: #f0f2f6;
}
div.stButton > button {
    width: 100%;
    background-color: red;
    color: white;
}
.login-box {
    background-color: white;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,0,0,0.1);
    width: 300px;
    margin: auto;
}
h2 {
    text-align: center;
    margin-bottom: 1.5rem;
    color: #333;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- HTML Content ---
st.markdown("<div class='login-box'>", unsafe_allow_html=True)
st.markdown("<h2>🔐 Login</h2>", unsafe_allow_html=True)

# --- Streamlit Inputs ---
username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")
login_btn = st.button("Login")

# --- Simple Authentication Logic ---
if login_btn:
    if username == "admin" and password == "1234":
        st.success("✅ Login successful!")
        st.balloons()
    else:
        st.error("❌ Invalid credentials. Try again.")

st.markdown("</div>", unsafe_allow_html=True)
