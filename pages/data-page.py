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

@st.cache_data
def prepare_dataframe(df):
    return df.to_csv()

with lcol:
    training_data = st.session_state["training_dataset"]
    st.header("Training Dataset (Full):")
    training_data

    if st.button(
        label = "Get training dataset",
        width = "stretch"
    ):        
        with st.spinner(
            text = "Preparing training data...",
            show_time = True
        ):
            training_data_csv = prepare_dataframe(training_data)
            st.session_state["training_data_csv"] = training_data_csv

    if "training_data_csv" in st.session_state:
        st.success("Training data ready for download! Click below:")

        st.download_button(
            label = "DOWNLOAD TRAINING DATA",
            data = st.session_state["training_data_csv"],
            file_name = "1repmatch-training-dataset-full.csv",
            type = "primary"
        )

with rcol:
    graph_data = st.session_state["chart_data"]
    st.header("Graph Dataset (Sampled):")
    graph_data

    if st.button(
        label = "Get graph dataset",
        width = "stretch"
    ):        
        with st.spinner(
            text = "Preparing graph data...",
            show_time = True
        ):
            graph_data_csv = prepare_dataframe(graph_data)
            st.session_state["graph_data_csv"] = graph_data_csv

    if "graph_data_csv" in st.session_state:
        st.success("Graph data ready for download! Click below:")

        st.download_button(
            label = "DOWNLOAD GRAPH DATA",
            data = st.session_state["graph_data_csv"],
            file_name = "1repmatch-graph-sampled-data.csv",
            type = "primary"
        )