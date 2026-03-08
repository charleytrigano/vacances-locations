import streamlit as st
from services.reservation_service import load_reservations
from services.calendar_service import build_calendar
from components.calendar_view import show_calendar

def show():

    st.title("Calendrier des réservations")

    df = load_reservations()

    calendar = build_calendar(df)

    show_calendar(calendar)
