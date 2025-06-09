import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(page_title="KLEIO - Your AI Fashion Stylist", layout="wide")
st.title("👗 KLEIO - AI Fashion Stylist & Wardrobe Assistant")

# -----------------------------
# Sidebar: User Input
# -----------------------------
st.sidebar.header("👤 Your Style Profile")

body_type = st.sidebar.selectbox("Body Type", ["Hourglass", "Pear", "Rectangle", "Apple", "Inverted Triangle"])
style_pref = st.sidebar.multiselect("Style Preferences", ["Casual", "Chic", "Bohemian", "Classic", "Streetwear", "Minimalist"])
budget = st.sidebar.slider("Budget Range (INR)", 500, 10000, (2000, 5000))

uploaded_image = st.sidebar.file_uploader("Upload Photo for Virtual Try-On", type=["jpg", "jpeg", "png"])

# -----------------------------
# Tab Layout
# -----------------------------
tabs = st.tabs(["Style Chatbot", "Capsule Wardrobe", "Virtual Try-On", "Sustainable Brands", "Wardrobe Care"])

# -----------------------------
# 1. Style Chatbot (LLM-powered)
# -----------------------------
with tabs[0]:
    st.subheader("💬 Your Personal Fashion Chatbot")
    user_input = st.text_input("Ask KLEIO for style advice:", "Suggest an outfit for a brunch with friends.")
    if st.button("Get Suggestion"):
        with st.spinner("Thinking stylishly..."):
            # Simulated AI response (you can replace with actual API call)
            st.markdown("""
            **KLEIO Says:** For a brunch with friends, try a flowy bohemian maxi dress in earthy tones. Pair it with nude sandals and minimal accessories. Add a straw hat for charm! 🌿
            """)

# -----------------------------
# 2. Capsule Wardrobe Generator
# -----------------------------
with tabs[1]:
    st.subheader("👚 Capsule Wardrobe Generator")
    st.markdown("_Here are 5 versatile outfit combinations based on your profile:_")
    capsule_items = [
        ("White Linen Shirt", "Blue Denim Jeans"),
        ("Black Turtleneck", "Grey Trousers"),
        ("Printed Blouse", "Khaki Skirt"),
        ("Oversized Blazer", "Cycling Shorts"),
        ("Graphic Tee", "Wide-Leg Pants")
    ]
    for top, bottom in capsule_items:
        st.write(f"👕 **{top}** + 👖 **{bottom}**")

# -----------------------------
# 3. Virtual Try-On (CV Simulation)
# -----------------------------
with tabs[2]:
    st.subheader("📸 Virtual Try-On Preview")
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Photo", width=300)
        st.success("Virtual try-on is enabled in the full version.")
        st.info("Note: AI-generated outfit overlay will be shown here with backend CV integration.")
    else:
        st.warning("Upload a photo from the sidebar to try outfits digitally.")

# -----------------------------
# 4. Sustainable Fashion Finder
# -----------------------------
with tabs[3]:
    st.subheader("🌱 Sustainable Brand Recommendations")
    eco_brands = [
        ("No Nasties", "https://www.nonasties.in"),
        ("Nicobar", "https://www.nicobar.com"),
        ("Okhai", "https://www.okhai.org"),
        ("Brown Living", "https://www.brownliving.in")
    ]
    for brand, link in eco_brands:
        st.markdown(f"✅ [{brand}]({link}) - Ethical & eco-conscious fashion")

# -----------------------------
# 5. Wardrobe Care Assistant
# -----------------------------
with tabs[4]:
    st.subheader("🧺 Wardrobe Care Tips")
    st.markdown("""
    * 👕 Wash clothes in cold water to reduce energy use.
    * 🧼 Use eco-friendly detergents.
    * 👗 Avoid over-washing delicate items.
    * 🧺 Store woolens in breathable bags.
    * ✂️ Repair before replacing!
    """)
    st.info("More care tips coming soon from KLEIO's AI wardrobe advisor!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("Made with ❤️ by Team TARA | Powered by GPT-4 & Streamlit")
