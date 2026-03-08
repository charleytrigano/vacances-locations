import streamlit as st
from services.reservation_service import load_reservations
from components.reservation_table import show_table

def show():

    st.title("Réservations")

    df = load_reservations()

    show_table(df)
