# ecommerce_laptop_app.py
import streamlit as st

# Sample data
laptops = [
    {"name": "Dell XPS 13", "price": 999, "brand": "Dell"},
    {"name": "MacBook Air M2", "price": 1199, "brand": "Apple"},
    {"name": "HP Pavilion", "price": 750, "brand": "HP"},
    {"name": "Lenovo ThinkPad X1", "price": 1300, "brand": "Lenovo"},
    {"name": "Asus ZenBook", "price": 950, "brand": "Asus"},
]

# Initialize session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("💻 Laptop eCommerce App")

# Sidebar filter
brands = list(set([l["brand"] for l in laptops]))
selected_brand = st.sidebar.selectbox("Filter by brand", ["All"] + brands)

# Filter laptops
if selected_brand != "All":
    filtered_laptops = [l for l in laptops if l["brand"] == selected_brand]
else:
    filtered_laptops = laptops

st.subheader("Available Laptops")

# Product display
for laptop in filtered_laptops:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**{laptop['name']}**")
        st.write(f"Brand: {laptop['brand']}")
        st.write(f"Price: ${laptop['price']}")
    with col2:
        if st.button(f"🛒 Add to Cart - {laptop['name']}"):
            st.session_state.cart.append(laptop)
            st.success(f"Added {laptop['name']} to cart!")

# Cart section
st.sidebar.subheader("🛍️ Shopping Cart")
total = sum(item["price"] for item in st.session_state.cart)
for item in st.session_state.cart:
    st.sidebar.write(f"- {item['name']} (${item['price']})")
st.sidebar.write("---")
st.sidebar.write(f"**Total: ${total}**")

# Clear cart button
if st.sidebar.button("❌ Clear Cart"):
    st.session_state.cart.clear()
    st.sidebar.success("Cart cleared!")
