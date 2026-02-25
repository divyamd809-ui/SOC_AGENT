def calculate_risk(threats):
    if len(threats) >= 2:
        return "High"
    elif len(threats) == 1:
        return "Medium"
    return "Low"