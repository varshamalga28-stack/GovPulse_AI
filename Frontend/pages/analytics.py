import streamlit as st
import pandas as pd
import plotly.express as px

from api import get_analytics


st.title("🏛️ GovPulse AI")
st.subheader("📈 Analytics")
st.caption("Complaint management analytics and insights")


# --------------------------------------------------
# GET DATA
# --------------------------------------------------

data = get_analytics()

if not data or "error" in data:
    st.error("Could not connect to the analytics backend.")

    if data:
        st.code(data.get("error", "Unknown error"))

    st.stop()


# --------------------------------------------------
# VALUES
# --------------------------------------------------

total_complaints = data.get("total_complaints", 0)
total_predictions = data.get("total_predictions", 0)
total_feedback = data.get("total_feedback", 0)
emergency_cases = data.get("emergency_cases", 0)
non_emergency_cases = data.get("non_emergency_cases", 0)


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

st.subheader("📊 Analytics Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Complaints", total_complaints)

with col2:
    st.metric("Total Predictions", total_predictions)

with col3:
    st.metric("Total Feedback", total_feedback)


st.divider()


# --------------------------------------------------
# CHART 1
# --------------------------------------------------

st.subheader("📊 Complaint Processing")

activity_data = pd.DataFrame({
    "Activity": [
        "Complaints",
        "Predictions",
        "Feedback"
    ],
    "Count": [
        total_complaints,
        total_predictions,
        total_feedback
    ]
})

fig1 = px.bar(
    activity_data,
    x="Activity",
    y="Count",
    text="Count",
    title="Complaint Processing Activity"
)

fig1.update_traces(textposition="outside")

fig1.update_layout(
    xaxis_title="",
    yaxis_title="Number of Records",
    height=450
)

st.plotly_chart(
    fig1,
    use_container_width=True
)


# --------------------------------------------------
# CHART 2
# --------------------------------------------------

st.subheader("🚨 Emergency Analysis")

emergency_data = pd.DataFrame({
    "Classification": [
        "Emergency",
        "Non-Emergency"
    ],
    "Count": [
        emergency_cases,
        non_emergency_cases
    ]
})

fig2 = px.pie(
    emergency_data,
    names="Classification",
    values="Count",
    hole=0.45,
    title="Emergency vs Non-Emergency Complaints"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# --------------------------------------------------
# CHART 3
# --------------------------------------------------

st.subheader("📈 Complaint Statistics")

statistics_data = pd.DataFrame({
    "Metric": [
        "Total Complaints",
        "Predictions",
        "Emergency",
        "Non-Emergency",
        "Feedback"
    ],
    "Count": [
        total_complaints,
        total_predictions,
        emergency_cases,
        non_emergency_cases,
        total_feedback
    ]
})

fig3 = px.line(
    statistics_data,
    x="Metric",
    y="Count",
    markers=True,
    title="GovPulse AI Statistics"
)

fig3.update_layout(
    xaxis_title="Metric",
    yaxis_title="Count",
    height=450
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


# --------------------------------------------------
# TABLE
# --------------------------------------------------

st.subheader("📋 Analytics Summary")

st.dataframe(
    statistics_data,
    use_container_width=True,
    hide_index=True
)


st.success("Analytics data is retrieved live from Supabase.")