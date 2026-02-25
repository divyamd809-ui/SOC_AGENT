def detect_threat(log):
    threats = []

    if "failed login" in log:
        threats.append("Brute Force Attempt")

    if "sql" in log:
        threats.append("SQL Injection")

    if "malware" in log:
        threats.append("Malware Activity")

    return threats