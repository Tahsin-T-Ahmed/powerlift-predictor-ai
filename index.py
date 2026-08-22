import streamlit as st

home_page = st.Page(
    page = "./pages/home.py", 
    title = "Home",
    icon = ":material/home:"
)

dev_page = st.Page(
    page = "./pages/dev.py",
    title = "Developer",
    icon = ":material/eyeglasses_2:"
)

nav = st.navigation(
    pages = [home_page, dev_page],
    position = "top"
)

nav.run()