import joblib
import streamlit as st

st.set_page_config(
    page_title = "1RepMatch: Predict Powerlifting Strength",
    layout = "wide"
)

st.title(
    body = "1RepMatch: Unlock your Powerlifting Potential",
    text_alignment = "center"
)
st.markdown(
    body = '#### "I know my max strength for only two lifts, but not the other one..."',
    text_alignment = "center"
)

st.divider()

lcol, mcol, rcol = st.columns((2, 2, 4))

with lcol:
    st.radio(
        label = "Which of the three scores are you MISSING?",
        options = [lift for lift in st.session_state["lifts"]],
        key = "target_lift",
        persist_state = "session"
    )

    predictor_lifts = [lift for lift in st.session_state["lifts"] if lift != st.session_state["target_lift"]]

    st.radio(
        label = "Select your GENDER:",
        options = ["Male", "Female"],
        key = "input_sex",
        persist_state = "session"
    )

    st.number_input(
        label = "How old are you?",
        min_value = 8,
        key = "input_age",
        value = 25
    )
    
    st.number_input(
        label = "Enter your weight (KG):",
        min_value = 10,
        key = "input_bodyweight",
        value = 75
    )

with mcol:

    for predictor_lift in predictor_lifts:
        st.number_input(
            label = f"Enter your max {predictor_lift}:",
            min_value = 0,
            key = f"input_{predictor_lift.lower()}",
            value = 100
        )

    st.button(
        label = f"Predict {st.session_state["target_lift"]}",
        width = "stretch",
        icon = ":material/touch_app:"
    )
    
with rcol:
    if "target_lift" in st.session_state:
        st.markdown(
            body = f"#### Correlation between {predictor_lifts[0]} and {predictor_lifts[1]}",
            text_alignment = "center"
        )
        st.scatter_chart(
            data = st.session_state["chart_data"],
            x = predictor_lifts[0].capitalize(),
            y = predictor_lifts[1].capitalize(),
            color = "Sex"
        )

        f"Chart (scatter-plot) created from {st.session_state["chart_data"].shape[0]} samples"
    else:
        "Select an exercise to predict your strength"

st.session_state

with st.bottom:
    "WARNING: These predictions are only estimates, and are not meant to be exact. Please exercise caution."