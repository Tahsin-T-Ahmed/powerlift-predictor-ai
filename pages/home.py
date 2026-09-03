import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title = "1RepMatch: Predict Powerlifting Strength",
    page_icon = ":material/fitness_center:",
    layout = "centered"
)

st.title(
    body = ":material/fitness_center: 1RepMatch",
    text_alignment = "center"
)
st.markdown(
    body = '#### Unlock your powerlifting potential!',
    text_alignment = "center"
)

with st.container(horizontal = True, horizontal_alignment = "center"):
    '"I know my strength for only two lifts, but not the other one..."'

# st.divider()

lcol, rcol = st.columns(2)

with lcol:
    lifts = st.session_state["lifts"]

    target_lift = st.radio(
        label = "Which of the three scores are you MISSING?",
        options = lifts,
        horizontal = True,
        key = "target_lift",
        persist_state = "session"
    )

    gender = st.radio(
        label = "Select your GENDER:",
        options = ["Male", "Female"],
        horizontal = True,
        key = "input_sex",
        persist_state = "session"
    )
    
    age = st.number_input(
        label = "Age:",
        min_value = 8,
        key = "input_age",
        value = 25
    )

with rcol:
    weight_unit = st.radio(
        label = "Preferred WEIGHT UNIT:",
        options = st.session_state["weight_units"],
        horizontal = True,
        key = "selected_weight_unit",
        persist_state = "session"
    )

    weight_unit_short = weight_unit.split(' ')[1]

    kg_lb_ratio = 0.45359237
    
    predictor_lifts = [lift for lift in lifts if lift != target_lift]

    bodyweight = st.number_input(
        label = f"Bodyweight {weight_unit_short}:",
        min_value = 10.0,
        key = "input_bodyweight",
        value = 75.0
    )
        

    predictor_lift_col1, predictor_lift_col2 = st.columns(2)

    for i, predictor_lift in enumerate(predictor_lifts):
        if 0 == i:
            col = predictor_lift_col1
        else:
            col = predictor_lift_col2

        with col:
            st.number_input(
                label = f"Max {predictor_lift} {weight_unit_short}:",
                min_value = 0.0,
                key = f"input_{predictor_lift.lower()}",
                value = 100.0
            )

@st.cache_resource
def load_model_and_scaler(target_lift):
    model = joblib.load(
        filename = f"./machine-learning/artifacts/models/{target_lift.lower()}-modelxgb.pkl"
    )

    scaler = joblib.load(
        filename = f"./machine-learning/artifacts/scalers/{target_lift.lower()}-scaler.joblib"
    )

    return model, scaler

if st.button(
    label = f"Predict {target_lift}",
    width = "stretch",
    icon = ":material/touch_app:",
    type = "primary"
):

    with st.spinner("Loading model and scaler... This will only take a few seconds."):
        model, scaler = load_model_and_scaler(target_lift)

    unit_multiplier = 1

    if "(lbs)" == weight_unit_short:
        unit_multiplier = kg_lb_ratio

    input_df = pd.DataFrame({
        "WEIGHT": st.session_state["input_bodyweight"] * unit_multiplier,
        f"{predictor_lifts[0]}": st.session_state[f"input_{predictor_lifts[0].lower()}"] * unit_multiplier,
        f"{predictor_lifts[1]}": st.session_state[f"input_{predictor_lifts[1].lower()}"] * unit_multiplier,
        "IS_MALE": int("Male" == st.session_state["input_sex"]),
        "AGE_DELTA_35": np.abs(st.session_state["input_age"] - 35),
    }, index=[1])

    numerical_predictors = [feature for feature in input_df.columns if feature != "IS_MALE"]
    input_df[numerical_predictors] = scaler.transform(
        pd.DataFrame(
            input_df[numerical_predictors],
            columns = numerical_predictors
        )
    )

    prediction_raw = model.predict(input_df).item()

    prediction = np.round(float(prediction_raw), 2)
    st.session_state["prediction"] = prediction

    st.markdown(
        body = f"# :red[{prediction}] {st.session_state['selected_weight_unit'].split(' ')[1][1:-1]}",
        text_alignment = "center"
    )
            
st.markdown(
    body = f"#### {predictor_lifts[0]}-{predictor_lifts[1]} correlation {weight_unit_short}",
    text_alignment = "center"
)

chart_data_clean = st.session_state["chart_data"]
chart_data = chart_data_clean.copy()

lifts_capitalized = [lift.capitalize() for lift in lifts]

if "(lbs)" == weight_unit_short:
    chart_data[lifts_capitalized] /= kg_lb_ratio
    chart_data[lifts_capitalized] = chart_data[lifts_capitalized].round(2)

st.scatter_chart(
    data = chart_data,
    x = predictor_lifts[0].capitalize(),
    y = predictor_lifts[1].capitalize(),
    color = st.session_state["target_lift"].capitalize()
)

st.caption(f"Charts created from {st.session_state['chart_data'].shape[0]} of {st.session_state['training_dataset'].shape[0]} samples")

with st.container(horizontal = True, horizontal_alignment = "center"):    
    f"WARNING: This app's predictions are only estimates. Please exercise with caution."

with st.container(horizontal = True, horizontal_alignment = "center"):
    "Made by [Tahsin Ahmed](https://github.com/Tahsin-T-Ahmed)"

    "[Github Repo](https://github.com/Tahsin-T-Ahmed/powerlift-predictor-ai)"