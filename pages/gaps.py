import streamlit as st
from services.reservation_service import load_reservations
from services.gap_service import detect_gaps

def show():

    st.title("Trous de réservation")

    df = load_reservations()

    gaps = detect_gaps(df)

    st.write(gaps)
