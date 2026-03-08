import streamlit as st

from components.sidebar import sidebar
from pages import dashboard, reservations, analytics

st.set_page_config(
    page_title="Vacances-Locations",
    layout="wide"
)

page = sidebar()

if page == "Dashboard":
    dashboard.show()

elif page == "Réservations":
    reservations.show()

elif page == "Analyses":
    analytics.show()
