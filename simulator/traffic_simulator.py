import random


def simulate_suspicious_traffic():
    """
    Generate a simulated suspicious network traffic event.

    This does NOT generate real network traffic.
    """

    source_ips = [
        "10.0.0.75",
        "10.0.0.85",
        "192.168.1.85",
        "192.168.1.95"
    ]

    target_ips = [
        "192.168.1.10",
        "192.168.1.20",
        "10.0.0.10"
    ]

    traffic_types = [
        "Unusual outbound traffic",
        "Abnormally high request rate",
        "Suspicious data transfer"
    ]

    source_ip = random.choice(source_ips)
    target = random.choice(target_ips)
    traffic_type = random.choice(traffic_types)

    request_count = random.randint(100, 500)

    return {
        "incident_type": "Suspicious Traffic",
        "source_ip": source_ip,
        "target": target,
        "traffic_type": traffic_type,
        "request_count": request_count,
        "description": (
            f"{traffic_type} detected. "
            f"{request_count} requests observed in the simulation."
        )
    }