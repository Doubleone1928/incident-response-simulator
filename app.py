from flask import Flask, render_template, redirect, url_for

from database.db import (
    init_db,
    get_incidents,
    get_incident_stats,
    get_incident_by_id,
    get_incident_type_stats,
    get_severity_stats,
    create_incident
)

from simulator.port_scan import simulate_port_scan
from simulator.auth_simulator import simulate_brute_force
from simulator.traffic_simulator import simulate_suspicious_traffic

from detection.detector import analyze_event

from response.response_engine import respond_to_incident


app = Flask(__name__)


# Initialize database
init_db()


@app.route("/")
def dashboard():
    stats = get_incident_stats()

    return render_template(
        "dashboard.html",
        stats=stats
    )


@app.route("/incidents")
def incidents():
    incidents = get_incidents()

    return render_template(
        "incidents.html",
        incidents=incidents
    )

@app.route("/incidents/<int:incident_id>")
def incident_detail(incident_id):

    incident = get_incident_by_id(incident_id)

    if incident is None:
        return "Incident not found", 404

    return render_template(
        "incident.html",
        incident=incident
    )
@app.route("/reports")
def reports():

    stats = get_incident_stats()

    type_stats = get_incident_type_stats()

    severity_stats = get_severity_stats()

    return render_template(
        "reports.html",
        stats=stats,
        type_stats=type_stats,
        severity_stats=severity_stats
    )


@app.route("/simulate/port-scan")
def simulate_port_scan_route():

    # Generate simulated port-scan event
    event = simulate_port_scan()

    # Analyze the event
    detection = analyze_event(event)

    # Create incident if detected
    if detection["detected"]:

        incident_id = create_incident(
            incident_type=event["incident_type"],
            source_ip=event["source_ip"],
            target=event["target"],
            severity=detection["severity"],
            detection_rule=detection["rule"],
            description=event["description"]
        )

        # Perform simulated response
        respond_to_incident(
            incident_id=incident_id,
            incident_type=event["incident_type"],
            source_ip=event["source_ip"],
            severity=detection["severity"]
        )

    return redirect(url_for("dashboard"))


@app.route("/simulate/brute-force")
def simulate_brute_force_route():

    # Generate simulated authentication event
    event = simulate_brute_force()

    # Analyze the event
    detection = analyze_event(event)

    # Create incident if detected
    if detection["detected"]:

        incident_id = create_incident(
            incident_type=event["incident_type"],
            source_ip=event["source_ip"],
            target=event["username"],
            severity=detection["severity"],
            detection_rule=detection["rule"],
            description=event["description"]
        )

        # Perform simulated response
        respond_to_incident(
            incident_id=incident_id,
            incident_type=event["incident_type"],
            source_ip=event["source_ip"],
            severity=detection["severity"]
        )

    return redirect(url_for("dashboard"))


@app.route("/simulate/traffic")
def simulate_traffic_route():

    # Generate simulated traffic event
    event = simulate_suspicious_traffic()

    # Analyze the event
    detection = analyze_event(event)

    # Create incident if detected
    if detection["detected"]:

        incident_id = create_incident(
            incident_type=event["incident_type"],
            source_ip=event["source_ip"],
            target=event["target"],
            severity=detection["severity"],
            detection_rule=detection["rule"],
            description=event["description"]
        )

        # Perform simulated response
        respond_to_incident(
            incident_id=incident_id,
            incident_type=event["incident_type"],
            source_ip=event["source_ip"],
            severity=detection["severity"]
        )

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)