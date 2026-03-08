import streamlit as st
import plotly.express as px
from services.reservation_service import load_reservations

def show():

    st.title("Analyses")

    df = load_reservations()

    df["mois"] = df["date_arrivee"].dt.month

    revenus = df.groupby("mois")["prix_total"].sum().reset_index()

    fig = px.bar(
        revenus,
        x="mois",
        y="prix_total",
        title="Revenus par mois"
    )

    st.plotly_chart(fig, use_container_width=True)
