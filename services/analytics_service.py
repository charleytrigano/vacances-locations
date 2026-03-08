def compute_kpis(df):

    ca_total = df["prix_total"].sum()

    nb_resa = len(df)

    nuits = df["nb_nuits"].sum()

    revenu_nuit = ca_total / nuits if nuits > 0 else 0

    return {
        "ca_total": ca_total,
        "nb_resa": nb_resa,
        "revenu_nuit": revenu_nuit
    }
