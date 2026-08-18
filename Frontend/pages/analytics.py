import streamlit as st

from api import get_analytics


# ============================================================
# PAGE TITLE
# ============================================================

st.title("📊 Analytics")

st.write(
    "AI Powered Government Complaint Management System"
)


# ============================================================
# LOAD DATA
# ============================================================

data = get_analytics()


# ============================================================
# ERROR HANDLING
# ============================================================

if not isinstance(data, dict):

    st.error("Invalid response received from backend.")

    st.write(data)

    st.stop()


if "error" in data:

    st.error("❌ Backend connection failed.")

    st.code(data["error"])

    st.info(
        "Backend URL: "
        "https://govpulse-ai-backend.onrender.com"
    )

    st.stop()


# ============================================================
# GET VALUES
# ============================================================

total_complaints = data.get(
    "total_complaints",
    0
)

total_predictions = data.get(
    "total_predictions",
    0
)

total_feedback = data.get(
    "total_feedback",
    0
)

emergency_cases = data.get(
    "emergency_cases",
    0
)

non_emergency_cases = data.get(
    "non_emergency_cases",
    0
)


# ============================================================
# METRICS
# ============================================================

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


# ============================================================
# EMERGENCY ANALYSIS
# ============================================================

st.divider()

st.subheader("🚨 Emergency Analysis")

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


# ============================================================
# CHART
# ============================================================

st.subheader("📈 Prediction Distribution")

chart_data = {
    "Emergency": emergency_cases,
    "Non-Emergency": non_emergency_cases
}

st.bar_chart(chart_data)


# ============================================================
# SUMMARY
# ============================================================

st.divider()

st.subheader("📋 System Summary")

st.write(
    f"""
    **Total Complaints:** {total_complaints}

    **Total Predictions:** {total_predictions}

    **Total Feedback:** {total_feedback}

    **Emergency Cases:** {emergency_cases}

    **Non-Emergency Cases:** {non_emergency_cases}
    """
)
