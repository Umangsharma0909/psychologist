import streamlit as st

# Website Configuration
st.set_page_config(
    page_title="SR Psychological Services",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for Responsive Design
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        color: #212529;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #0056b3;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #004085;
    }
    .sidebar .sidebar-content {
        background-color: #f1f3f4;
    }
    @media (max-width: 768px) {
        .main {
            font-size: 14px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 8px 16px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Select a Page:", ["Home", "Services", "About Us", "Contact Us"])

# Home Page
if page == "Home":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.title("Welcome to SR Psychological Services")
        st.write(
            "At SR Psychological Services, we offer compassionate and evidence-based care "
            "to help you achieve emotional well-being and mental clarity."
        )
        if st.button("Explore Our Services"):
            st.sidebar.radio("Select a Page:", ["Services"], index=0)

# Services Page
elif page == "Services":
    st.title("Our Services")
    service_details = {
        "Individual Therapy": "Personalized sessions to address anxiety, depression, and stress.",
        "Couples Therapy": "Helping couples enhance communication and resolve conflicts.",
        "Family Therapy": "Supporting families to improve relationships and dynamics.",
        "Group Therapy": "A supportive environment to share and learn together.",
        "Online Therapy": "Convenient sessions from the comfort of your home.",
    }
    for i, (service, description) in enumerate(service_details.items(), start=1):
        st.markdown(f"### {i}. {service}")
        st.write(description)
        if st.checkbox(f"Learn more about {service}", key=i):
            st.write(f"More detailed information about {service} is coming soon!")

# About Us Page
elif page == "About Us":
    st.title("About Us")
    st.write(
        "SR Psychological Services is led by Dr. Sarah Roberts, a licensed clinical psychologist "
        "with over 20 years of experience in mental health care."
    )
    st.markdown("### Why Choose Us?")
    st.write(
        "- Empathy and understanding are at the core of our practice.\n"
        "- We use evidence-based techniques tailored to your needs.\n"
        "- Your privacy and confidentiality are guaranteed."
    )

# Contact Us Page
elif page == "Contact Us":
    st.title("Contact Us")
    st.markdown("### Get in Touch")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Submit"):
            st.success("Thank you for reaching out! We will get back to you soon.")

    st.markdown("### Location")
    st.map(data=None, zoom=12, use_container_width=True)

    # Social Media Buttons (Interactive Element)
    st.markdown("### Follow Us")
    cols = st.columns(3)
    with cols[0]:
        st.button("Facebook")
    with cols[1]:
        st.button("Instagram")
    with cols[2]:
        st.button("LinkedIn")

# Footer
st.sidebar.write("**Follow Us:**")
st.sidebar.write("[Facebook](#) | [Instagram](#) | [LinkedIn](#)")
