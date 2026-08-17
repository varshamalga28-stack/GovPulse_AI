import streamlit as st
import requests
from config import BASE_URL

st.title("🚨 Emergency Complaint Prediction")
st.caption("Analyze citizen complaints using the AI Emergency Detection Model")

st.divider()

# -----------------------------
# Input Section
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    customer_name = st.text_input(
        "👤 Customer Name",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "📧 Email",
        placeholder="example@gmail.com"
    )

with col2:

    phone = st.text_input(
        "📱 Phone Number",
        placeholder="9876543210"
    )

st.markdown("### Complaint")

complaint = st.text_area(
    "",
    placeholder="Describe your complaint here...",
    height=180
)

st.divider()

if st.button("🚀 Predict Complaint", use_container_width=True):

    if customer_name == "":
        st.warning("Enter Customer Name")

    elif email == "":
        st.warning("Enter Email")

    elif phone == "":
        st.warning("Enter Phone Number")

    elif complaint == "":
        st.warning("Enter Complaint")

    else:

        payload = {

            "complaint": complaint,

            "customer_name": customer_name,

            "email": email,

            "phone": phone

        }

        with st.spinner("Analyzing Complaint..."):

            response = requests.post(

                f"{BASE_URL}/api/predict",

                json=payload

            )

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]

            confidence = result["confidence"]

            st.success("Prediction Completed Successfully")

            st.divider()

            c1, c2 = st.columns(2)

            with c1:

                if prediction == 1:

                    st.error("🚨 Emergency Complaint")

                else:

                    st.success("✅ Non-Emergency Complaint")

            with c2:

                st.metric(

                    "Confidence",

                    f"{confidence*100:.2f}%"

                )

            st.progress(confidence)

            st.subheader("Complaint Summary")

            st.info(complaint)

        else:

            st.error("Prediction Failed")

            st.code(response.text)