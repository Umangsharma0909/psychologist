import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Website Configuration
st.set_page_config(
    page_title="Clinical Psychologist",
    page_icon="🎤",
    layout="wide"
)

# Custom CSS for Better UI
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
        color: #333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .sidebar .sidebar-content {
        background-color: #eef0f1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Services", "About Us", "Contact Us"])

# Home Page
if page == "Home":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Welcome to Our Clinical Psychology Practice</h1>
            <p style="font-size: 18px;">We provide care to improve your mental well-being and help you lead a balanced life.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image(caption="Providing Care for Your Mental Well-being", use_column_width=True)
    st.markdown("### Why Choose Us?")
    st.write(
        "- Experienced professionals with a compassionate approach.\n"
        "- Customized therapy plans designed for your unique needs.\n"
        "- A safe and confidential environment for healing."
    )
    st.markdown("### Quick Tips for Mental Health")
    st.write(
        "1. Practice mindfulness daily.\n"
        "2. Stay connected with loved ones.\n"
        "3. Engage in physical activity.\n"
        "4. Seek help when needed."
    )

# Services Page
elif page == "Services":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Our Services</h1>
            <p style="font-size: 18px;">Explore our range of professional services tailored to your needs.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image(caption="Explore Our Range of Services", use_column_width=True)
    service_details = {
        "Individual Therapy": "Personalized one-on-one sessions to address anxiety, depression, stress, and other challenges.",
        "Couples Therapy": "Helping couples strengthen their relationships and navigate conflicts.",
        "Family Therapy": "Supporting families to improve communication and resolve interpersonal challenges.",
        "Workshops and Seminars": "Regular sessions on mental health awareness, stress management, and mindfulness.",
        "Online Therapy": "Flexible and convenient therapy sessions from the comfort of your home.",
        "Group Therapy": "Join a supportive community to share experiences and strategies for mental well-being."
    }
    for service, description in service_details.items():
        st.markdown(f"### {service}")
        st.write(description)

# About Us Page
elif page == "About Us":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>About Us</h1>
            <p style="font-size: 18px;">Learn more about our philosophy and dedicated team.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image(caption="Meet Your Trusted Psychologist", use_column_width=True)
    st.write(
        "Our lead psychologist, Dr. Alex Taylor, holds over 15 years of experience in clinical psychology. "
        "With a passion for mental health, Dr. Taylor has helped countless individuals and families overcome challenges "
        "and achieve a better quality of life."
    )
    st.markdown("### Our Philosophy")
    st.write(
        "- **Empathy:** We understand and respect your experiences.\n"
        "- **Confidentiality:** Your privacy is our priority.\n"
        "- **Evidence-Based Care:** We use proven methods to achieve results."
    )

# Contact Us Page
elif page == "Contact Us":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Contact Us</h1>
            <p style="font-size: 18px;">We'd love to hear from you! Please fill out the form below to get in touch.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            st.success(f"Thank you, {name}! We will get back to you soon.")

    st.markdown("### Location")
    st.write("123 Mental Wellness Street, Suite 456, YourCity, YourCountry")
    st.map(data=None, zoom=None, use_container_width=True)

# Footer
st.sidebar.write("\n\n")
st.sidebar.write("**Contact Us:**")
st.sidebar.write("Email: info@psychologypractice.com")
st.sidebar.write("Phone: +123 456 7890")

