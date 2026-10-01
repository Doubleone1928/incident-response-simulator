<<<<<<< HEAD
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
=======
# incident-response-simulator
A Python Flask-based cybersecurity incident response simulator for detecting and responding to simulated security incidents.
>>>>>>> 1fafd5a070801ec5d9cf183bf7d0fd47d0f55581
# Incident Response Simulator

A safe, educational cybersecurity incident-response simulation tool built with **Python, Flask, SQLite, and pytest**.

The project simulates common security incidents, detects them using configurable detection rules, records incidents in a database, and performs safe simulated response actions.

> **Safety:** This project is designed for simulation and education. It does not attack real machines, block real IP addresses, or lock real user accounts.

---

## Project Overview

The Incident Response Simulator demonstrates a basic security monitoring and incident-response workflow:

```text
Simulated Security Event
          ↓
       Detection
          ↓
       Incident
          ↓
       Database
          ↓
   Simulated Response
          ↓
       Dashboard
```

The application provides a web dashboard where users can generate simulated security incidents and view their results.

---

## Features

### 1. Port Scan Simulation

Generates a simulated port-scan event containing information such as:

* Source IP address
* Target IP address
* Number of ports scanned

The detection engine identifies the event when the number of scanned ports reaches the configured threshold.

Detection rule:

```text
PORT_SCAN_DETECTED
```

Simulated response:

```text
Simulated IP blocked
```

---

### 2. Brute Force Simulation

Generates a simulated authentication attack containing:

* Username
* Source IP address
* Number of failed login attempts

Detection rule:

```text
BRUTE_FORCE_DETECTED
```

Simulated response:

```text
Simulated account temporarily locked
```

---

### 3. Suspicious Traffic Simulation

Generates simulated unusually high network traffic.

The event contains:

* Source IP address
* Target
* Request count

Detection rule:

```text
SUSPICIOUS_TRAFFIC_DETECTED
```

Simulated response:

```text
Simulated suspicious traffic source contained
```

---

## Dashboard

The dashboard provides an overview of simulated security incidents, including:

* Total incidents
* Critical incidents
* Detected incidents
* Resolved incidents
* Incident visualizations

---

## Incident Management

The application provides an incidents page where users can:

* View all detected incidents
* View incident type
* View source IP
* View target
* View severity
* View status
* View response action
* View creation time

Each incident can also be opened to view its detailed information, including the detection rule and response.

---

## Reports

The Reports page provides a summary of incidents by:

* Incident type
* Severity

Charts are used to make the incident data easier to understand.

---

## Technologies

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Application logic         |
| Flask      | Web application framework |
| SQLite     | Incident database         |
| HTML       | Web interface             |
| CSS        | User interface styling    |
| JavaScript | Dashboard functionality   |
| pytest     | Automated testing         |
| Git/GitHub | Version control           |

---

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

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Doubleone1928/incident-response-simulator.git
```

Enter the project directory:

```bash
cd incident-response-simulator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```cmd
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## Running the Tests

Run the complete automated test suite:

```bash
python -m pytest -v
```

The project currently contains tests for:

* Detection rules
* Incident database operations
* Simulated response actions

Expected result:

```text
9 passed
```

---

## Detection Rules

The simulator currently uses the following thresholds:

| Incident           |           Threshold | Severity |
| ------------------ | ------------------: | -------- |
| Port Scan          |           20+ ports | HIGH     |
| Brute Force        | 10+ failed attempts | HIGH     |
| Suspicious Traffic |       300+ requests | MEDIUM   |

These values are used only by the simulation and detection engine.

---

## Incident Response

When an incident is detected, the response engine performs a **simulated** response.

| Incident Type      | Simulated Response                            |
| ------------------ | --------------------------------------------- |
| Port Scan          | Simulated IP blocked                          |
| Brute Force        | Simulated account temporarily locked          |
| Suspicious Traffic | Simulated suspicious traffic source contained |

No real network blocking or account modification is performed.

---

## Testing

Automated tests help verify that the main components continue working as new features are added.

The test suite covers:

```text
Detection
   ↓
Incident Database
   ↓
Response Engine
```

Current test status:

```text
9 tests passed
```

---

## Educational Purpose

This project was developed as a cybersecurity/software-development learning project to demonstrate:

* Security event simulation
* Rule-based detection
* Incident management
* Automated response concepts
* Database management
* Flask web development
* Software testing
* Git/GitHub version control

---

## Disclaimer

This project is intended for **educational and defensive security simulation purposes only**.

All security events and response actions are simulated. The project should not be used to attack, disrupt, or gain unauthorized access to real systems.

---

## Author

**Perez Lucky**

GitHub:

https://github.com/Doubleone1928
