import streamlit as st

# Constants
HEATING_VALUE = 38.6
CORRECTION_FACTOR = 1.013
DEFAULT_COST = 0.03784

st.title("Gas Usage Calculator")

prev = st.number_input("Previous Reading (m³)", value=0.0)
curr = st.number_input("Current Reading (m³)", value=0.0)
cost_per_mj = st.number_input("Cost per MJ ($)", value=DEFAULT_COST)

if st.button("Calculate Usage"):
    if curr > prev:
        volume_used = curr - prev
        mj_used = volume_used * HEATING_VALUE * CORRECTION_FACTOR
        cost = mj_used * cost_per_mj

        st.success(f"Gas Used: {volume_used:.2f} m³")
        st.info(f"MJ Used: {mj_used:.2f} MJ")
        st.info(f"Estimated Cost: ${cost:.2f}")
    else:
        st.warning("Current reading must be greater than previous.")