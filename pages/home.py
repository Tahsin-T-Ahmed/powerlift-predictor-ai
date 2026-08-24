import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title = "1RepMatch: Predict Powerlifting Strength",
    layout = "centered"
)

st.title(
    body = "1RepMatch: Unlock your Powerlifting Potential",
    text_alignment = "center"
)
st.markdown(
    body = '#### "I know my strength for only two lifts, but not the other one..."',
    text_alignment = "center"
)

st.divider()

lcol, rcol = st.columns(2)

with lcol:
    st.radio(
        label = "Which of the three scores are you MISSING?",
        options = [lift for lift in st.session_state["lifts"]],
        horizontal = True,
        key = "target_lift",
        persist_state = "session"
    )

    predictor_lifts = [lift for lift in st.session_state["lifts"] if lift != st.session_state["target_lift"]]

    st.radio(
        label = "Select your GENDER:",
        options = ["Male", "Female"],
        horizontal = True,
        key = "input_sex",
        persist_state = "session"
    )

    st.number_input(
        label = "How old are you?",
        min_value = 8.0,
        key = "input_age",
        value = 25.0
    )

with rcol:
    st.radio(
        label = "Preferred WEIGHT UNIT:",
        options = ["Kilograms (kg)", "Pounds (lbs)"],
        horizontal = True,
        key = "weight_unit",
        persist_state = "session"
    )
    
    st.number_input(
        label = f"Enter your BODYWEIGHT {st.session_state['weight_unit'].split(' ')[1]}:",
        min_value = 10.0,
        key = "input_bodyweight",
        value = 75.0
    )

    lift_col1, lift_col2 = st.columns(2)

    for i, predictor_lift in enumerate(predictor_lifts):
        if 0 == i:
            col = lift_col1
        else:
            col = lift_col2

        with col:
            st.number_input(
                label = f"Max {predictor_lift} {st.session_state['weight_unit'].split(' ')[1]}:",
                min_value = 0.0,
                key = f"input_{predictor_lift.lower()}",
                value = 100.0
            )

st.subheader(
    body = "Done? Click below:",
    text_alignment = "center"
)

if st.button(
    label = f"Predict {st.session_state["target_lift"]}",
    width = "stretch",
    icon = ":material/touch_app:"
):
    target = st.session_state["target_lift"]

    unit_multiplier = 1

    if "lbs" in st.session_state["weight_unit"]:
        unit_multiplier = 0.45359237

    input_df = pd.DataFrame({
        "WEIGHT": st.session_state["input_bodyweight"] * unit_multiplier,
        f"{predictor_lifts[0]}": st.session_state[f"input_{predictor_lifts[0].lower()}"] * unit_multiplier,
        f"{predictor_lifts[1]}": st.session_state[f"input_{predictor_lifts[1].lower()}"] * unit_multiplier,
        "IS_MALE": int("Male" == st.session_state["input_sex"]),
        "AGE_DELTA_35": np.abs(st.session_state["input_age"] - 30),
    }, index=[1])

    numerical_predictors = [feature for feature in input_df.columns if feature != "IS_MALE"]

    prediction = "Prediction"
    st.session_state["prediction"] = prediction

    st.markdown(
        body = f"### Estimated {target}: :red[{prediction}] {st.session_state['weight_unit'].split(' ')[1][1:-1]}",
        text_alignment = "center"
    )
            
    st.markdown(
        body = f"#### Correlation between {predictor_lifts[0]} and {predictor_lifts[1]}",
        text_alignment = "center"
    )
st.scatter_chart(
    data = st.session_state["chart_data"],
    x = predictor_lifts[0].capitalize(),
    y = predictor_lifts[1].capitalize(),
    color = st.session_state["target_lift"].capitalize()
)

st.caption(f"Charts created from {st.session_state['chart_data'].shape[0]} of {st.session_state['training_dataset'].shape[0]} samples")

with st.container(horizontal = True, horizontal_alignment = "center"):    
    f"WARNING: This app's predictions are only estimates. Please exercise with caution."