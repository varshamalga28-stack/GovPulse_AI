import streamlit as st
import pandas as pd

from api import get_feedback, submit_feedback


st.title("💬 Feedback")
st.caption("Customer feedback management")


# ==========================
# Submit Feedback
# ==========================

st.subheader("⭐ Submit Feedback")

prediction_id = st.number_input(
    "Prediction ID",
    min_value=1,
    value=1,
    step=1
)

rating = st.slider(
    "Rating",
    1,
    5,
    5
)

feedback_text = st.text_area(
    "Feedback"
)


if st.button("Submit Feedback"):

    if not feedback_text.strip():

        st.warning("Please enter feedback.")

    else:

        result = submit_feedback(
            prediction_id,
            rating,
            feedback_text
        )

        if "error" in result:

            st.error("Could not submit feedback.")
            st.code(result["error"])

        else:

            st.success(
                result.get(
                    "message",
                    "Feedback submitted successfully"
                )
            )

            st.rerun()


# ==========================
# Feedback History
# ==========================

st.divider()

st.subheader("📋 Feedback History")

data = get_feedback()

if "error" in data:

    st.error("Unable to load feedback.")
    st.code(data["error"])

else:

    records = data.get("feedback", [])

    if records:

        st.success(
            f"{len(records)} feedback records found."
        )

        df = pd.DataFrame(records)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No feedback found.")