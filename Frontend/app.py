import streamlit as st
from style import load_css

st.set_page_config(
    page_title="GovPulse AI",
    page_icon="\U0001F916",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Application logo
st.logo(
    "https://img.icons8.com/color/96/artificial-intelligence.png"
)

# Main header
st.markdown(
    '<h1 class="main-title">\U0001F3DB\ufe0f GovPulse AI</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI Powered Government Complaint Management System</p>',
    unsafe_allow_html=True
)

# Navigation
pg = st.navigation([
    st.Page(
        "pages/dashboard.py",
        title="Dashboard",
        icon="\U0001F4CA"
    ),
    st.Page(
        "pages/prediction.py",
        title="Prediction",
        icon="\U0001F916"
    ),
    st.Page(
        "pages/history.py",
        title="History",
        icon="\U0001F4DC"
    ),
    st.Page(
        "pages/analytics.py",
        title="Analytics",
        icon="\U0001F4C8"
    ),
    st.Page(
        "pages/feedback.py",
        title="Feedback",
        icon="\U0001F4AC"
    ),
])

pg.run()