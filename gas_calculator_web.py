import streamlit as st
from datetime import datetime, date, time

# Constants
HEATING_VALUE = 38.6
CORRECTION_FACTOR = 1.013
DEFAULT_COST = 0.03784
DEFAULT_DAILY_CHARGE = 0.95  # in dollars

st.set_page_config(page_title="Gas Usage Calculator", layout="centered")
st.title("📊 Gas Usage Calculator")

# Session state initialization
if "first_reading" not in st.session_state:
    st.session_state.first_reading = None
if "first_timestamp" not in st.session_state:
    st.session_state.first_timestamp = None
if "first_date" not in st.session_state:
    st.session_state.first_date = date.today()
if "first_time" not in st.session_state:
    st.session_state.first_time = datetime.now().time()

# --- Section 1: Set First Meter Reading ---
st.subheader("1. Set First Meter Reading")

first = st.number_input("Initial Meter Reading (m³)", value=0.0, key="first_input")
first_date = st.date_input("Date of First Reading", value=st.session_state.first_date)
first_time = st.time_input("Time of First Reading", value=st.session_state.first_time)

if st.button("Save First Reading"):
    st.session_state.first_reading = first
    st.session_state.first_date = first_date
    st.session_state.first_time = first_time
    dt_str = datetime.combine(first_date, first_time).strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.first_timestamp = dt_str
    st.success(f"✅ Saved: {first:.2f} m³ at {dt_str}")

# --- Section 2: Current Reading and Cost Inputs ---
if st.session_state.first_reading is not None:
    st.subheader("2. Enter Current Reading and Cost Info")
    st.info(f"📌 First reading: {st.session_state.first_reading:.2f} m³ on {st.session_state.first_timestamp}")

    current = st.number_input("Current Meter Reading (m³)", value=0.0)
    current_date = st.date_input("Date of Current Reading", value=date.today())

    cost_per_mj = st.number_input(
        "Cost per MJ ($)", value=DEFAULT_COST, step=0.00001, format="%.5f"
    )

    daily_charge = st.number_input(
        "Daily Supply Charge ($/day)", value=DEFAULT_DAILY_CHARGE, step=0.0001, format="%.4f"
    )

    if st.button("Calculate Usage"):
        if current > st.session_state.first_reading:
            # Core calculation
            volume_used = current - st.session_state.first_reading
            mj_used = volume_used * HEATING_VALUE * CORRECTION_FACTOR
            usage_cost = mj_used * cost_per_mj

            # Days used
            days_used = (current_date - st.session_state.first_date).days
            supply_cost = days_used * daily_charge
            total_cost = usage_cost + supply_cost

            # Output results
            st.success(f"📏 Gas Used: {volume_used:.2f} m³")
            st.info(f"🔥 MJ Used: {mj_used:.2f} MJ")
            st.info(f"💸 Usage Cost: ${usage_cost:.2f}")
            st.info(f"⚡ Supply Charges ({days_used} days @ ${daily_charge:.4f}): ${supply_cost:.2f}")
            st.success(f"🧾 **Total Estimated Cost: ${total_cost:.2f}**")
        else:
            st.warning("⚠️ Current reading must be greater than the first reading.")
else:
    st.warning("⚠️ Please save a first reading above before continuing.")
