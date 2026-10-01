from detection.detector import analyze_event


def test_port_scan_detection():
    event = {
        "incident_type": "Port Scan",
        "source_ip": "10.0.0.25",
        "target": "192.168.1.10",
        "ports_scanned": 25,
        "description": "Simulated port scan"
    }

    result = analyze_event(event)

    assert result["detected"] is True
    assert result["severity"] == "HIGH"
    assert result["rule"] == "PORT_SCAN_DETECTED"


def test_brute_force_detection():
    event = {
        "incident_type": "Brute Force",
        "source_ip": "10.0.0.45",
        "username": "admin",
        "failed_attempts": 12,
        "description": "Simulated brute-force attack"
    }

    result = analyze_event(event)

    assert result["detected"] is True
    assert result["severity"] == "HIGH"
    assert result["rule"] == "BRUTE_FORCE_DETECTED"


def test_suspicious_traffic_detection():
    event = {
        "incident_type": "Suspicious Traffic",
        "source_ip": "10.0.0.75",
        "target": "192.168.1.20",
        "request_count": 350,
        "description": "Simulated suspicious traffic"
    }

    result = analyze_event(event)

    assert result["detected"] is True
    assert result["severity"] == "MEDIUM"
    assert result["rule"] == "SUSPICIOUS_TRAFFIC_DETECTED"


def test_normal_port_scan_is_not_detected():
    event = {
        "incident_type": "Port Scan",
        "source_ip": "10.0.0.25",
        "target": "192.168.1.10",
        "ports_scanned": 5,
        "description": "Normal simulated scan"
    }

    result = analyze_event(event)

    assert result["detected"] is False