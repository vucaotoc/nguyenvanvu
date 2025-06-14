import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Setup ---
st.set_page_config(page_title="📊 Visualization", layout="wide")

st.title("📈 Laptop Sales Visualization")

# --- Sample Data ---
@st.cache_data
def load_data():
    data = {
        "Laptop": ["Dell XPS", "MacBook Air", "HP Pavilion", "Lenovo X1", "Asus ZenBook"],
        "Sales": [150, 200, 180, 220, 170]
    }
    return pd.DataFrame(data)

df = load_data()

# --- Bar Chart ---
st.subheader("🛍️ Sales by Product")
fig1, ax1 = plt.subplots()
ax1.bar(df["Laptop"], df["Sales"])
ax1.set_ylabel("Units Sold")
ax1.set_title("Laptop Sales Bar Chart")
st.pyplot(fig1)

# --- Pie Chart ---
st.subheader("📊 Market Share")
fig2, ax2 = plt.subplots()
ax2.pie(df["Sales"], labels=df["Laptop"], autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)
