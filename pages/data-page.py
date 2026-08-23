import streamlit as st

st.set_page_config(
    page_title = "1RepMatch: Data",
    layout = "wide"
)

st.title("1RepMatch: Data")
st.subheader("Datasets used in this application:")

lcol, rcol = st.columns(2)

with lcol:
    st.header("Training Dataset (Full):")
    st.session_state["training_dataset"]

with rcol:
    st.header("Graph Data (Sampled):")
    st.session_state["chart_data"]