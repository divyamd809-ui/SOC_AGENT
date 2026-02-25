from agents.normalizer import normalize_log
from agents.detector import detect_threat
from agents.correlator import correlate
from agents.risk_engine import calculate_risk

def process_log(log):

    normalized = normalize_log(log)
    threats = detect_threat(normalized)
    attack_type = correlate(threats)
    risk = calculate_risk(threats)

    return {
        "normalized_log": normalized,
        "threats_detected": threats,
        "attack_type": attack_type,
        "risk_level": risk
    }