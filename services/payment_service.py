def payment_status(row):

    if row["acompte"] == 0:
        return "acompte manquant"

    if row["acompte"] < row["prix_total"]:
        return "solde restant"

    return "payé"
