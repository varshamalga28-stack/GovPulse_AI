import streamlit as st
import pandas as pd

from api import get_prediction_history


st.title("📜 Prediction History")

st.subheader(
    "View all previous complaint predictions"
)

st.divider()


data = get_prediction_history()


# ------------------------------------------------------------
# Error
# ------------------------------------------------------------

if not isinstance(data, dict):

    st.error("Invalid response received from backend.")
    st.write(data)
    st.stop()


if "error" in data:

    st.error("Unable to load prediction history.")

    st.code(
        data.get("error", "Unknown error")
    )

    if "details" in data:
        st.code(data["details"])

    st.stop()


# ------------------------------------------------------------
# Extract history
# ------------------------------------------------------------

history = data.get(
    "history",
    []
)


total = data.get(
    "total_predictions",
    len(history)
)


st.metric(
    "Total Predictions",
    total
)


st.divider()


if not history:

    st.info(
        "No prediction history found."
    )

else:

    df = pd.DataFrame(history)

    # Move important columns first
    preferred_columns = [
        "id",
        "complaint_id",
        "prediction",
        "category",
        "subcategory",
        "department",
        "severity",
        "priority",
        "sentiment",
        "issue_type",
        "product",
        "confidence",
        "predicted_at"
    ]

    available_columns = [
        col for col in preferred_columns
        if col in df.columns
    ]

    remaining_columns = [
        col for col in df.columns
        if col not in available_columns
    ]

    df = df[
        available_columns +
        remaining_columns
    ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
