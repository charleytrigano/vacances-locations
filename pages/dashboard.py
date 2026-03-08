import streamlit as st
from services.reservation_service import load_reservations
from services.analytics_service import compute_kpis
from components.kpi_cards import show_kpis

def show():

    st.title("Dashboard")

    df = load_reservations()

    kpis = compute_kpis(df)

    show_kpis(kpis)

    st.subheader("Réservations récentes")

    st.dataframe(df.tail(10))
