import pandas as pd
from database.reservations_repo import insert_reservation

def import_csv(file):

    df = pd.read_csv(file)

    for _, row in df.iterrows():

        reservation = {
            "client_nom": row["guest"],
            "date_arrivee": row["checkin"],
            "date_depart": row["checkout"],
            "prix_total": row["price"]
        }

        insert_reservation(reservation)
