import streamlit as st
import pandas as pd

from api import get_analytics, get_prediction_history


# =========================================================
# PAGE HEADER
# =========================================================

st.title("🏛️ GovPulse AI")
st.subheader("📊 Dashboard")
st.caption("AI Powered Government Complaint Management System")


# =========================================================
# ANALYTICS SUMMARY
# =========================================================

data = get_analytics()

if not data or "error" in data:

    st.error("Dashboard could not connect to the backend.")

    if data:
        st.code(data.get("error", "Unknown error"))

else:

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total Complaints",
        data.get("total_complaints", 0)
    )

    col2.metric(
        "Predictions",
        data.get("total_predictions", 0)
    )

    col3.metric(
        "Feedback",
        data.get("total_feedback", 0)
    )

    col4.metric(
        "Emergency",
        data.get("emergency_cases", 0)
    )

    col5.metric(
        "Non-Emergency",
        data.get("non_emergency_cases", 0)
    )


# =========================================================
# COMPLAINT HISTORY
# =========================================================

st.divider()

st.subheader("📚 Complaint History")

st.caption("View recently submitted complaints and their predictions.")

history_data = get_prediction_history()

if not history_data or "error" in history_data:

    st.info("No complaints submitted yet.")

else:

    history = history_data.get("history", [])

    if len(history) == 0:

        st.info("No complaints submitted yet.")

    else:

        # Show latest records first
        rows = []

        for item in history:

            rows.append({
                "ID": item.get("id"),
                "Complaint ID": item.get("complaint_id"),
                "Category": item.get("category"),
                "Subcategory": item.get("subcategory"),
                "Department": item.get("department"),
                "Severity": item.get("severity"),
                "Priority": item.get("priority"),
                "Sentiment": item.get("sentiment"),
                "Confidence": (
                    f"{item.get('confidence')}%"
                    if item.get("confidence") is not None
                    else "N/A"
                ),
                "Predicted At": item.get("predicted_at")
            })

        history_df = pd.DataFrame(rows)

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# SYSTEM INFORMATION
# =========================================================

st.divider()

st.subheader("ℹ️ System Information")


col1, col2 = st.columns(2)


# ---------------------------------------------------------
# AI MODULES
# ---------------------------------------------------------

with col1:

    st.markdown("### 🤖 AI Modules Used")

    modules = [
        "Module 1 - Complaint Reason Classification",
        "Module 2 - Department Classification",
        "Module 3 - Sentiment Analysis",
        "Module 4 - Feedback Category Classification",
        "Module 5 - Priority Prediction",
        "Module 6 - Emergency Detection",
        "Module 7 - Harmful Content Detection",
        "Module 8 - Trend Forecasting",
        "Module 9 - Anomaly Detection",
        "Module 10 - Government Action Recommendation"
    ]

    for module in modules:
        st.markdown(f"✅ {module}")


# ---------------------------------------------------------
# TECHNOLOGY STACK
# ---------------------------------------------------------

with col2:

    st.markdown("### 💻 Technology Stack")

    technologies = [
        "Streamlit",
        "FastAPI",
        "Supabase",
        "PostgreSQL",
        "Scikit-learn",
        "Pandas",
        "NumPy",
        "Joblib",
        "Python",
        "Machine Learning"
    ]

    for technology in technologies:
        st.markdown(f"• {technology}")


# =========================================================
# PROJECT SUMMARY
# =========================================================

st.divider()

st.subheader("📌 Project Summary")

st.markdown(
    """
    **GovPulse AI** is an AI-powered government complaint management
    system designed to analyze citizen complaints and assist in
    identifying emergency cases, complaint categories, priorities,
    departments and other useful insights.

    The system provides:

    - 📝 Complaint submission
    - 🤖 AI-based complaint prediction
    - 🚨 Emergency detection
    - 📊 Analytics and visualization
    - 📚 Prediction history
    - ⭐ Citizen feedback
    - 🗄️ Supabase database integration
    - ⚡ FastAPI backend
    - 🖥️ Streamlit frontend
    """
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "GovPulse AI • AI Powered Government Complaint Management System"
)