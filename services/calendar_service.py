def reservations_to_events(df):

    events = []

    for _, row in df.iterrows():

        events.append({
            "title": row["client_nom"],
            "start": str(row["date_arrivee"]),
            "end": str(row["date_depart"]),
            "resourceId": row["appartement"]
        })

    return events
