def detect_gaps(df):

    df = df.sort_values("date_arrivee")

    gaps = []

    for i in range(len(df) - 1):

        depart = df.iloc[i]["date_depart"]
        arrivee = df.iloc[i+1]["date_arrivee"]

        diff = (arrivee - depart).days

        if diff > 1:

            gaps.append({
                "start": depart,
                "end": arrivee,
                "nuits": diff
            })

    return gaps
