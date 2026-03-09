def financial_summary(df):

    total_revenue = df["prix_total"].sum()

    monthly = df.groupby(
        df["date_arrivee"].dt.month
    )["prix_total"].sum()

    avg_stay = df["nb_nuits"].mean()

    return {
        "revenue": total_revenue,
        "monthly": monthly,
        "avg_stay": avg_stay
    }
