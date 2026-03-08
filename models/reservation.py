from dataclasses import dataclass
from datetime import date

@dataclass
class Reservation:

    id: int
    appartement_id: int
    client_nom: str
    client_email: str

    date_arrivee: date
    date_depart: date

    prix_total: float
    acompte: float
    statut_paiement: str
