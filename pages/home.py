import streamlit as st

st.set_page_config(
    page_title = "1RepMatch: Predict Powerlifting Strength"
)

st.title("1RepMatch")
st.header("Unlock your Powerlifting potential!")
st.markdown('#### "I know my max score for only two lifts, but not the other one..."')

st.divider()

lcol, rcol = st.columns((2, 3))

with lcol:
    st.radio(
        label = "Which of the three lift scores are you MISSING?",
        options = [lift for lift in st.session_state["lifts"]],
        key = "target_lift",
        persist_state = "session"
    )

    predictor_lifts = [lift for lift in st.session_state["lifts"] if lift != st.session_state["target_lift"]]

# @st.cache_data
def show_scatterplot(feature1, feature2):
    st.scatter_chart(
        data = st.session_state["chart_data"],
        x = feature1,
        y = feature2,
        color = "Sex"
    )
    
with rcol:
    if "target_lift" in st.session_state:
        show_scatterplot(
            feature1 = predictor_lifts[0].capitalize(),
            feature2 = predictor_lifts[1].capitalize()
        )
    else:
        "Select an exercise to predict your strength"

with st.bottom:
    "WARNING: These predictions are only estimates, and are not meant to be exact. Please exercise caution."