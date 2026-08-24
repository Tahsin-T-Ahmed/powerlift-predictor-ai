import joblib
import pandas as pd
import streamlit as st

home_page = st.Page(
    page = "./pages/home.py", 
    title = "Home",
    icon = ":material/home:"
)

data_page = st.Page(
    page = "./pages/data-page.py",
    title = "Data",
    icon = ":material/data_table:"
)

dev_page = st.Page(
    page = "./pages/dev.py",
    title = "Developer",
    icon = ":material/eyeglasses_2:"
)

nav = st.navigation(
    pages = [home_page, data_page, dev_page],
    position = "top"
)

@st.cache_resource
def load_dataset():
    dataset = pd.read_csv(
        "./machine-learning/datasets/training-dataset.csv",
        index_col = 0
    )

    return dataset

@st.cache_resource
def load_chart_data():
    chart_data = st.session_state["training_dataset"].sample(n=1000)

    return chart_data

with st.spinner(
    text = "Loading data... This will only take a few seconds",
    show_time = True
):
    st.session_state["training_dataset"] = load_dataset()
    st.session_state["chart_data"] = load_chart_data()

st.session_state["lifts"] = ["SQUAT", "BENCH", "DEADLIFT"]

st.session_state["weight_units"] = ["Kilograms (kg)", "Pounds (lbs)"]

nav.run()