# Incident Response Simulator

A cybersecurity incident-response simulation tool built with Python and Flask.

## Project Overview

The Incident Response Simulator demonstrates how a security monitoring system can detect simulated security incidents, create incident records, and perform safe simulated response actions.

The project does **not** attack real machines or perform real-world blocking.

## Features

The simulator currently supports three simulated incident types:

1. **Port Scan**

   * Simulates scanning multiple ports.
   * Detection rule: `PORT_SCAN_DETECTED`
   * Response: `Simulated IP blocked`

2. **Brute Force Authentication**

   * Simulates repeated failed login attempts.
   * Detection rule: `BRUTE_FORCE_DETECTED`
   * Response: `Simulated account temporarily locked`

3. **Suspicious Traffic**

   * Simulates unusually high request traffic.
   * Detection rule: `SUSPICIOUS_TRAFFIC_DETECTED`
   * Response: `Simulated suspicious traffic source contained`

## System Flow

```text
Simulated Security Event
          |
          v
     Detection Engine
          |
          v
       Incident
          |
          v
       Database
          |
          v
    Response Engine
          |
          v
   Contained Incident
          |
          v
 Dashboard / Reports
```

## Technologies

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript
* pytest

## Project Structure

```text
incident-response-simulator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   └── config.py
│
├── simulator/
│   ├── __init__.py
│   ├── port_scan.py
│   ├── traffic_simulator.py
│   └── auth_simulator.py
│
├── detection/
│   ├── __init__.py
│   ├── rules.py
│   └── detector.py
│
├── response/
│   ├── __init__.py
│   └── response_engine.py
│
├── database/
│   ├── __init__.py
│   ├── models.py
│   └── db.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── incidents.html
│   ├── incident.html
│   └── reports.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
│
└── tests/
    ├── test_detection.py
    ├── test_response.py
    └── test_incidents.py
```

## Installation

Create and activate a virtual environment:

```text
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```text
pip install -r requirements.txt
```

## Running the Application

Start Flask with:

```text
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Running the Tests

Run the automated tests with:

```text
python -m pytest -v
```

The current test suite verifies the detection engine, database operations, and simulated response engine.

## Safety

This project is designed for educational and laboratory use.
