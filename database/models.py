from dataclasses import dataclass
from typing import Optional


@dataclass
class Incident:
    incident_type: str
    source_ip: str
    severity: str
    target: Optional[str] = None
    description: Optional[str] = None
    status: str = "detected"
    response_action: Optional[str] = None