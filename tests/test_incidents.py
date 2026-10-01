from database.db import (
    get_db_connection,
    create_incident,
    get_incident_by_id
)


def test_create_and_get_incident():

    connection = get_db_connection()

    cursor = connection.execute(
        """
        INSERT INTO incidents (
            incident_type,
            source_ip,
            target,
            severity,
            detection_rule,
            description
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            "Test Incident",
            "10.0.0.99",
            "192.168.1.99",
            "LOW",
            "TEST_RULE",
            "Test incident created by pytest"
        )
    )

    incident_id = cursor.lastrowid

    connection.commit()
    connection.close()

    incident = get_incident_by_id(incident_id)

    assert incident is not None
    assert incident["incident_type"] == "Test Incident"
    assert incident["source_ip"] == "10.0.0.99"
    assert incident["severity"] == "LOW"
    assert incident["detection_rule"] == "TEST_RULE"


def test_create_incident_function():

    incident_id = create_incident(
        incident_type="Test Port Scan",
        source_ip="10.0.0.88",
        target="192.168.1.88",
        severity="HIGH",
        detection_rule="PORT_SCAN_DETECTED",
        description="Testing incident creation"
    )

    incident = get_incident_by_id(incident_id)

    assert incident is not None
    assert incident["incident_type"] == "Test Port Scan"
    assert incident["detection_rule"] == "PORT_SCAN_DETECTED"