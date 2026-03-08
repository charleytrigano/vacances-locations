from datetime import datetime, timedelta

def upcoming_arrivals(df):

    today = datetime.today()

    return df[
        (df["date_arrivee"] >= today) &
        (df["date_arrivee"] <= today + timedelta(days=2))
    ]
