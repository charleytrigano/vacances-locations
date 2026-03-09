import streamlit as st

def sidebar():

    st.sidebar.title("🏡 Vacances-Locations")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Réservations",
            "Calendrier",
            "Analyses",
            "Opportunités",
            "Ménage",
            "Messages",
            "Paramètres"
        ]
    )

    return page
