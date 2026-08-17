import streamlit as st
import pandas as pd
import plotly.express as px

from api import get_analytics


st.title("📊 Analytics")

st.subheader(
    "GovPulse AI Complaint Analytics"
)

st.divider()


data = get_analytics()


# ------------------------------------------------------------
# Error handling
# ------------------------------------------------------------

if not isinstance(data, dict):

    st.error(
        "Invalid analytics response."
    )

    st.write(data)

    st.stop()


if "error" in data:

    st.error(
        "Unable to load analytics."
    )

    st.code(
        data.get("error", "Unknown error")
    )

    if "details" in data:
        st.code(data["details"])

    st.stop()


# ------------------------------------------------------------
# Values
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# Metrics
# ------------------------------------------------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Complaints",
    total_complaints
)

c2.metric(
    "Predictions",
    total_predictions
)

c3.metric(
    "Feedback",
    total_feedback
)


st.divider()


# ------------------------------------------------------------
# Emergency chart
# ------------------------------------------------------------

chart_data = pd.DataFrame({
    "Type": [
        "Emergency",
        "Non-Emergency"
    ],
    "Count": [
        emergency_cases,
        non_emergency_cases
    ]
})


fig = px.bar(
    chart_data,
    x="Type",
    y="Count",
    title="Emergency vs Non-Emergency Complaints",
    text="Count"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


st.subheader("Prediction Summary")

st.dataframe(
    chart_data,
    use_container_width=True,
    hide_index=True
)
