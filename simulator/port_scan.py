import random


def simulate_port_scan():
    """
    Generate a simulated port-scan security event.
    This does NOT perform a real network scan.
    """

    source_ips = [
        "10.0.0.25",
        "10.0.0.50",
        "192.168.1.25",
        "192.168.1.50"
    ]

    target_ips = [
        "192.168.1.10",
        "192.168.1.20",
        "10.0.0.10"
    ]

    source_ip = random.choice(source_ips)
    target = random.choice(target_ips)

    ports_scanned = random.randint(15, 50)

    return {
        "incident_type": "Port Scan",
        "source_ip": source_ip,
        "target": target,
        "ports_scanned": ports_scanned,
        "description": (
            f"Simulated port scan detected. "
            f"{ports_scanned} ports were scanned."
        )
    }