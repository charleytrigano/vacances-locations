def cleaning_schedule(df):

    cleanings = []

    for _, row in df.iterrows():

        cleanings.append({
            "appartement": row["appartement"],
            "date": row["date_depart"],
            "type": "ménage"
        })

    return cleanings
