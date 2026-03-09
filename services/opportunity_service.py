def suggest_price(base_price, occupation_rate):

    if occupation_rate > 0.8:
        return base_price * 1.2

    if occupation_rate < 0.4:
        return base_price * 0.8

    return base_price
