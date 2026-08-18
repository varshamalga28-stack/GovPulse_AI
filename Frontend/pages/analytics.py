import streamlit as st
from api import get_analytics


st.title("📊 Analytics")

st.write("Government Complaint Analytics")


# Get analytics data
data = get_analytics()


# ------------------------------------------------------------
# Error handling
# ------------------------------------------------------------

if not isinstance(data, dict):

    st.error("Invalid response received from backend.")

    st.write(data)

    st.stop()


if "error" in data:

    st.error("Dashboard could not connect to the backend.")

    st.code(data["error"])

    st.stop()


# ------------------------------------------------------------
# Read values
# ------------------------------------------------------------

total_complaints = data.get("total_complaints", 0)
total_predictions = data.get("total_predictions", 0)
total_feedback = data.get("total_feedback", 0)
emergency_cases = data.get("emergency_cases", 0)
non_emergency_cases = data.get("non_emergency_cases", 0)


# ------------------------------------------------------------
# Metrics
# ------------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Complaints",
        total_complaints
    )

with col2:
    st.metric(
        "Total Predictions",
        total_predictions
    )

with col3:
    st.metric(
        "Total Feedback",
        total_feedback
    )


st.divider()


col4, col5 = st.columns(2)

with col4:
    st.metric(
        "Emergency Cases",
        emergency_cases
    )

with col5:
    st.metric(
        "Non-Emergency Cases",
        non_emergency_cases
    )


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

st.subheader("📈 Prediction Summary")

if total_predictions > 0:

    chart_data = {
        "Emergency": emergency_cases,
        "Non-Emergency": non_emergency_cases
    }

    st.bar_chart(chart_data)

else:

    st.info("No predictions available yet.")
