import streamlit as st

st.set_page_config(
    page_title = "1RepMatch: About the Developer",
    page_icon = ":material/fitness_center:"
)

st.title(
    body = ":material/fitness_center: 1RepMatch: Developer",
    text_alignment = "center"
)

lcol, rcol = st.columns(2)

with lcol:
    st.image(
        image = "./img/tahsin-muscle-pic.png"
    )

with rcol:
    st.header("Hi! I'm [Tahsin](https://github.com/Tahsin-T-Ahmed).")
    "I'm a programmer, gym-goer, cat-lover, music-maker, jiu-jitsu athlete, and freemason."
    "Just kidding. I don't know jiu-jitsu."
    
    "Anyway, my journey began when I accidentally ended up in a Web Development major in college."
    "Originally, my interest was 3D CGI. I didn't want to code, I wanted to make the next Kung Fu Panda!"
    "But I fell in love with programming, and eventually went to grad school for Machine Learning."

    st.markdown(
        body = "##### Let's connect!", 
        text_alignment = "right"
    )
    
    st.markdown(
        body = "###### [LinkedIn: tahsin-t-ahmed](https://www.linkedin.com/in/tahsin-t-ahmed/)", 
        text_alignment = "right"
    )
    
    st.markdown(
        body = "###### [GitHub: tahsin-t-ahmed](https://github.com/Tahsin-T-Ahmed)", 
        text_alignment = "right"
    )
    
    