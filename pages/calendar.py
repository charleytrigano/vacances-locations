import streamlit as st
from services.reservation_service import load_reservations

def show():

    st.title("Calendrier")

    df = load_reservations()

    st.write(df[["appartement","date_arrivee","date_depart"]])
