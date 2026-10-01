from database.db import create_incident, get_db_connection
import response.response_engine as response_engine


def test_port_scan_response():
    incident_id = create_incident(
        incident_type="Port Scan",
        source_ip="10.0.0.25",
        severity="HIGH"
    )

    result = response_engine.respond_to_incident(
        incident_id=incident_id,
        incident_type="Port Scan",
        source_ip="10.0.0.25",
        severity="HIGH"
    )

    assert result["status"] == "contained"
    assert result["response_action"] == "Simulated IP blocked"

    connection = get_db_connection()

    incident = connection.execute(
        """
        SELECT status, response_action
        FROM incidents
        WHERE id = ?
        """,
        (incident_id,)
    ).fetchone()

    connection.close()

    assert incident["status"] == "contained"
    assert incident["response_action"] == "Simulated IP blocked"


def test_brute_force_response():
    incident_id = create_incident(
        incident_type="Brute Force",
        source_ip="10.0.0.45",
        severity="HIGH"
    )

    result = response_engine.respond_to_incident(
        incident_id=incident_id,
        incident_type="Brute Force",
        source_ip="10.0.0.45",
        severity="HIGH"
    )

    assert result["status"] == "contained"
    assert result["response_action"] == (
        "Simulated account temporarily locked"
    )

    connection = get_db_connection()

    incident = connection.execute(
        """
        SELECT status, response_action
        FROM incidents
        WHERE id = ?
        """,
        (incident_id,)
    ).fetchone()

    connection.close()

    assert incident["status"] == "contained"
    assert incident["response_action"] == (
        "Simulated account temporarily locked"
    )


def test_suspicious_traffic_response():
    incident_id = create_incident(
        incident_type="Suspicious Traffic",
        source_ip="10.0.0.75",
        severity="MEDIUM"
    )

    result = response_engine.respond_to_incident(
        incident_id=incident_id,
        incident_type="Suspicious Traffic",
        source_ip="10.0.0.75",
        severity="MEDIUM"
    )

    assert result["status"] == "contained"
    assert result["response_action"] == (
        "Simulated suspicious traffic source contained"
    )

    connection = get_db_connection()

    incident = connection.execute(
        """
        SELECT status, response_action
        FROM incidents
        WHERE id = ?
        """,
        (incident_id,)
    ).fetchone()

    connection.close()

    assert incident["status"] == "contained"
    assert incident["response_action"] == (
        "Simulated suspicious traffic source contained"
    )