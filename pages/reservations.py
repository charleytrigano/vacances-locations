import streamlit as st
from services.reservation_service import load_reservations

def show():

    st.title("Réservations")

    df = load_reservations()

    st.dataframe(df, use_container_width=True)
