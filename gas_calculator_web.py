import streamlit as st
from datetime import datetime

# Constants
HEATING_VALUE = 38.6
CORRECTION_FACTOR = 1.013
DEFAULT_COST = 0.03784

st.title("Gas Usage Calculator")

# Session state for saved reading
if "first_reading" not in st.session_state:
    st.session_state.first_reading = None
if "first_time" not in st.session_state:
    st.session_state.first_time = None

# Save a first reading with timestamp
st.subheader("Set First Reading")
first = st.number_input("Enter Initial Meter Reading (m³)", value=0.0, key="first_input")

if st.button("Save First Reading"):
    st.session_state.first_reading = first
    st.session_state.first_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success(f"Initial reading saved: {first} m³ at {st.session_state.first_time}")

# Show stored reading
if st.session_state.first_reading is not None:
    st.info(f"Saved first reading: {st.session_state.first_reading} m³ on {st.session_state.first_time}")
    current = st.number_input("Enter Current Meter Reading (m³)", value=0.0)
    cost_per_mj = st.number_input("Cost per MJ ($)", value=DEFAULT_COST)

    if st.button("Calculate Usage"):
        if current > st.session_state.first_reading:
            volume_used = current - st.session_state.first_reading
            mj_used = volume_used * HEATING_VALUE * CORRECTION_FACTOR
            cost = mj_used * cost_per_mj

            st.success(f"Gas Used: {volume_used:.2f} m³")
            st.info(f"MJ Used: {mj_used:.2f} MJ")
            st.info(f"Estimated Cost: ${cost:.2f}")
        else:
            st.warning("Current reading must be greater than the first reading.")
else:
    st.warning("Please save a first reading before continuing.")
