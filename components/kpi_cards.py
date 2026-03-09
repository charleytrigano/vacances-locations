import streamlit as st

def show_kpis(kpis: dict):
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 CA Net",        f"{kpis.get('ca_net', kpis.get('ca_total', 0)):.0f} €")
    col2.metric("📅 Réservations",  kpis.get("nb_reservations", kpis.get("nb_resa", 0)))
    col3.metric("📈 Revenu / nuit", f"{kpis.get('revenu_nuit', 0):.0f} €")