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

st.session_state["training_dataset"] = pd.read_csv(
    "./machine-learning/datasets/training-dataset.csv",
    index_col = 0
)

st.session_state["chart_data"] = st.session_state["training_dataset"].sample(n=1000)

st.session_state["lifts"] = ["SQUAT", "BENCH", "DEADLIFT"]

nav.run()