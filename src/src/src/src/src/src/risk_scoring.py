def calculate_risk(probability):

    score = probability * 100

    if score > 80:
        risk = "HIGH"
    elif score > 50:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return score, risk