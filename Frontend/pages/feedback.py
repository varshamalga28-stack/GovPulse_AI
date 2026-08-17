import streamlit as st
import pandas as pd

from api import (
    get_feedback,
    submit_feedback
)


st.title("💬 Feedback")

st.subheader(
    "Submit and view citizen feedback"
)

st.divider()


# ============================================================
# Submit Feedback
# ============================================================

st.subheader("📝 Submit Feedback")


prediction_id = st.number_input(
    "Prediction ID",
    min_value=1,
    step=1
)


rating = st.slider(
    "Rating",
    min_value=1,
    max_value=5,
    value=5
)


feedback_text = st.text_area(
    "Feedback",
    placeholder="Enter your feedback..."
)


if st.button(
    "Submit Feedback",
    type="primary"
):

    if not feedback_text.strip():

        st.warning(
            "Please enter feedback."
        )

    else:

        result = submit_feedback(
            int(prediction_id),
            int(rating),
            feedback_text
        )

        if isinstance(result, dict) and "error" in result:

            st.error(
                "Unable to submit feedback."
            )

            st.code(
                result.get("error", "")
            )

            if "details" in result:
                st.code(result["details"])

        else:

            st.success(
                "Feedback submitted successfully!"
            )


st.divider()


# ============================================================
# Existing Feedback
# ============================================================

st.subheader(
    "📋 Previous Feedback"
)


data = get_feedback()


if not isinstance(data, dict):

    st.error(
        "Invalid feedback response."
    )

    st.write(data)

    st.stop()


if "error" in data:

    st.error(
        "Unable to load feedback."
    )

    st.code(
        data.get("error", "Unknown error")
    )

    if "details" in data:
        st.code(data["details"])

    st.stop()


feedback_list = data.get(
    "feedback",
    []
)


total_feedback = data.get(
    "total_feedback",
    len(feedback_list)
)


st.metric(
    "Total Feedback",
    total_feedback
)


if not feedback_list:

    st.info(
        "No feedback submitted yet."
    )

else:

    df = pd.DataFrame(
        feedback_list
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
