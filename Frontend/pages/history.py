import streamlit as st
import pandas as pd

from api import get_prediction_history


st.title("📜 Prediction History")
st.caption("View previous complaint predictions")

data = get_prediction_history()

if "error" in data:

    st.error("Unable to load prediction history.")
    st.code(data["error"])

else:

    history = data.get("history", [])

    if not history:

        st.info("No prediction history found.")

    else:

        st.success(
            f"Total predictions: {len(history)}"
        )

        df = pd.DataFrame(history)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )