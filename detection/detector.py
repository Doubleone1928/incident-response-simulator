from detection.rules import (
    detect_port_scan,
    detect_brute_force,
    detect_suspicious_traffic
)


def analyze_event(event):
    """
    Analyze a simulated security event
    and determine whether it is suspicious.
    """

    incident_type = event.get("incident_type")

    if incident_type == "Port Scan":
        return detect_port_scan(event)

    if incident_type == "Brute Force":
        return detect_brute_force(event)

    if incident_type == "Suspicious Traffic":
        return detect_suspicious_traffic(event)

    return {
        "detected": False,
        "severity": "LOW",
        "rule": None
    }