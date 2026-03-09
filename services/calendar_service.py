import pandas as pd

def build_calendar(df):

    calendar = []

    for _, row in df.iterrows():

        calendar.append({
            "appartement": row["appartement"],
            "start": row["date_arrivee"],
            "end": row["date_depart"],
            "client": row["client_nom"]
        })

    return pd.DataFrame(calendar)
