def generate_cleaning(df):

    cleanings = df[["appartement", "date_depart"]]

    cleanings = cleanings.rename(
        columns={"date_depart": "date_menage"}
    )

    return cleanings
