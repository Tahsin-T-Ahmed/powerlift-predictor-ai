import streamlit as st

st.set_page_config(
    page_title = "1RepMatch: Data",
    page_icon = ":material/fitness_center:",
    layout = "wide"
)

st.title(
    body = ":material/fitness_center: 1RepMatch: Data",
    text_alignment = "center"
)
st.subheader(
    body = "Datasets used in this application (kg units):",
    text_alignment = "center"
)

st.divider()

lcol, rcol = st.columns(2)

with lcol:
    st.header("Training Dataset (Full):")
    st.session_state["training_dataset"]

with rcol:
    st.header("Graph Data (Sampled):")
    st.session_state["chart_data"]