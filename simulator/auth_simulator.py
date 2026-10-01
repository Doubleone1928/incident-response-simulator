import random


def simulate_brute_force():
    """
    Generate a simulated brute-force authentication event.

    This does NOT attempt real logins.
    """

    usernames = [
        "admin",
        "administrator",
        "user",
        "test"
    ]

    source_ips = [
        "10.0.0.45",
        "10.0.0.55",
        "192.168.1.45",
        "192.168.1.75"
    ]

    username = random.choice(usernames)
    source_ip = random.choice(source_ips)

    failed_attempts = random.randint(5, 20)

    return {
        "incident_type": "Brute Force",
        "username": username,
        "source_ip": source_ip,
        "failed_attempts": failed_attempts,
        "description": (
            f"Simulated brute-force activity detected. "
            f"{failed_attempts} failed login attempts "
            f"for user '{username}'."
        )
    }