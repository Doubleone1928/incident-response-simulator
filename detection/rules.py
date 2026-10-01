PORT_SCAN_THRESHOLD = 20


def detect_port_scan(event):
    ports_scanned = event.get("ports_scanned", 0)

    if ports_scanned >= PORT_SCAN_THRESHOLD:
        return {
            "detected": True,
            "severity": "HIGH",
            "rule": "PORT_SCAN_DETECTED"
        }

    return {
        "detected": False,
        "severity": "LOW",
        "rule": None
    }


BRUTE_FORCE_THRESHOLD = 10


def detect_brute_force(event):
    failed_attempts = event.get("failed_attempts", 0)

    if failed_attempts >= BRUTE_FORCE_THRESHOLD:
        return {
            "detected": True,
            "severity": "HIGH",
            "rule": "BRUTE_FORCE_DETECTED"
        }

    return {
        "detected": False,
        "severity": "LOW",
        "rule": None
    }
TRAFFIC_THRESHOLD = 300


def detect_suspicious_traffic(event):
    """
    Detect unusually high simulated traffic.
    """

    request_count = event.get("request_count", 0)

    if request_count >= TRAFFIC_THRESHOLD:
        return {
            "detected": True,
            "severity": "MEDIUM",
            "rule": "SUSPICIOUS_TRAFFIC_DETECTED"
        }

    return {
        "detected": False,
        "severity": "LOW",
        "rule": None
    }