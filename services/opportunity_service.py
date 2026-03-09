def booking_opportunities(gaps):

    opportunities = []

    for gap in gaps:

        if gap["nuits"] >= 3:

            opportunities.append({
                "start": gap["start"],
                "end": gap["end"],
                "type": "séjour court possible"
            })

    return opportunities
