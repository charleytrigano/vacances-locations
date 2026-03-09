import pandas as pd
from services.payment_service import payment_status

def load_reservations():

    df = pd.read_csv("data/reservations.csv")

    df["date_arrivee"] = pd.to_datetime(df["date_arrivee"])
    df["date_depart"] = pd.to_datetime(df["date_depart"])

    df["nb_nuits"] = (df["date_depart"] - df["date_arrivee"]).dt.days

    df["statut_paiement"] = df.apply(payment_status, axis=1)

    return df
