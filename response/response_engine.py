from database.db import get_db_connection


def respond_to_incident(
    incident_id,
    incident_type,
    source_ip,
    severity
):
    """
    Perform a safe simulated response to an incident.

    No real network blocking or account modification is performed.
    """

    if incident_type == "Port Scan":
        response_action = "Simulated IP blocked"

    elif incident_type == "Brute Force":
        response_action = "Simulated account temporarily locked"

    elif incident_type == "Suspicious Traffic":
        response_action = "Simulated suspicious traffic source contained"

    else:
        response_action = "Simulated incident contained"

    status = "contained"

    connection = get_db_connection()

    connection.execute(
        """
        UPDATE incidents
        SET status = ?,
            response_action = ?
        WHERE id = ?
        """,
        (
            status,
            response_action,
            incident_id
        )
    )

    connection.commit()
    connection.close()

    return {
        "status": status,
        "response_action": response_action,
        "source_ip": source_ip,
        "severity": severity
    }