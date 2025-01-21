import streamlit as st
from PIL import Image

# Website Configuration
st.set_page_config(
    page_title="Clinical Psychologist",
    page_icon="🎤",
    layout="wide"
)

# Load Images (Replace 'image_path.jpg' with your image paths)
home_image = Image.open("home_image.jpg")
services_image = Image.open("services_image.jpg")
about_image = Image.open("about_image.jpg")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Services", "About Us"])

# Home Page
if page == "Home":
    st.title("Welcome to Our Clinical Psychology Practice")
    st.image(home_image, caption="Providing Care for Your Mental Well-being", use_column_width=True)
    st.write(
        "We offer evidence-based psychological services tailored to your needs. "
        "Our mission is to help you achieve emotional well-being and a balanced life."
    )

# Services Page
elif page == "Services":
    st.title("Our Services")
    st.image(services_image, caption="Explore Our Range of Services", use_column_width=True)
    st.markdown("### Individual Therapy")
    st.write(
        "Personalized one-on-one sessions to address anxiety, depression, stress, and other challenges."
    )
    st.markdown("### Couples Therapy")
    st.write(
        "Helping couples strengthen their relationships and navigate conflicts."
    )
    st.markdown("### Family Therapy")
    st.write(
        "Supporting families to improve communication and resolve interpersonal challenges."
    )
    st.markdown("### Workshops and Seminars")
    st.write(
        "Regular sessions on mental health awareness, stress management, and mindfulness."
    )

# About Us Page
elif page == "About Us":
    st.title("About Us")
    st.image(about_image, caption="Meet Your Trusted Psychologist", use_column_width=True)
    st.write(
        "Our lead psychologist, Dr. Alex Taylor, holds over 15 years of experience in clinical psychology. "
        "With a passion for mental health, Dr. Taylor has helped countless individuals and families overcome challenges "
        "and achieve a better quality of life."
    )
    st.write(
        "At our practice, we value empathy, confidentiality, and a commitment to helping you on your journey "
        "to emotional well-being."
    )

# Footer
st.sidebar.write("\n\n")
st.sidebar.write("**Contact Us:**")
st.sidebar.write("Email: info@psychologypractice.com")
st.sidebar.write("Phone: +123 456 7890")
