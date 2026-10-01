import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "incident_response.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            incident_type TEXT NOT NULL,
            source_ip TEXT NOT NULL,
            target TEXT,
            severity TEXT NOT NULL,
            detection_rule TEXT,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'detected',
            response_action TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Add detection_rule to an existing database if it does not have it
    columns = connection.execute(
        "PRAGMA table_info(incidents)"
    ).fetchall()

    column_names = [column["name"] for column in columns]

    if "detection_rule" not in column_names:
        connection.execute(
            "ALTER TABLE incidents ADD COLUMN detection_rule TEXT"
        )

    connection.commit()
    connection.close()


def create_incident(
    incident_type,
    source_ip,
    severity,
    detection_rule=None,
    target=None,
    description=None,
    status="detected",
    response_action=None
):
    connection = get_db_connection()

    cursor = connection.execute(
        """
        INSERT INTO incidents (
            incident_type,
            source_ip,
            target,
            severity,
            detection_rule,
            description,
            status,
            response_action
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            incident_type,
            source_ip,
            target,
            severity,
            detection_rule,
            description,
            status,
            response_action
        )
    )

    connection.commit()

    incident_id = cursor.lastrowid

    connection.close()

    return incident_id


def get_incidents():
    connection = get_db_connection()

    incidents = connection.execute(
        """
        SELECT *
        FROM incidents
        ORDER BY created_at DESC
        """
    ).fetchall()

    connection.close()

    return incidents


def get_incident_by_id(incident_id):
    connection = get_db_connection()

    incident = connection.execute(
        """
        SELECT *
        FROM incidents
        WHERE id = ?
        """,
        (incident_id,)
    ).fetchone()

    connection.close()

    return incident

def get_incident_stats():
    connection = get_db_connection()

    total = connection.execute(
        "SELECT COUNT(*) FROM incidents"
    ).fetchone()[0]

    critical = connection.execute(
        "SELECT COUNT(*) FROM incidents WHERE severity = 'CRITICAL'"
    ).fetchone()[0]

    high = connection.execute(
        "SELECT COUNT(*) FROM incidents WHERE severity = 'HIGH'"
    ).fetchone()[0]

    medium = connection.execute(
        "SELECT COUNT(*) FROM incidents WHERE severity = 'MEDIUM'"
    ).fetchone()[0]

    detected = connection.execute(
        "SELECT COUNT(*) FROM incidents WHERE status = 'detected'"
    ).fetchone()[0]

    contained = connection.execute(
        "SELECT COUNT(*) FROM incidents WHERE status = 'contained'"
    ).fetchone()[0]

    resolved = connection.execute(
        "SELECT COUNT(*) FROM incidents WHERE status = 'resolved'"
    ).fetchone()[0]

    connection.close()

    return {
        "total": total,
        "critical": critical,
        "high": high,
        "medium": medium,
        "detected": detected,
        "contained": contained,
        "resolved": resolved
    }
def get_incident_type_stats():
    connection = get_db_connection()

    rows = connection.execute(
        """
        SELECT incident_type, COUNT(*) AS count
        FROM incidents
        GROUP BY incident_type
        ORDER BY count DESC
        """
    ).fetchall()

    connection.close()

    return rows


def get_severity_stats():
    connection = get_db_connection()

    rows = connection.execute(
        """
        SELECT severity, COUNT(*) AS count
        FROM incidents
        GROUP BY severity
        ORDER BY count DESC
        """
    ).fetchall()

    connection.close()

    return rows