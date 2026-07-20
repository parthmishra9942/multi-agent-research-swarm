from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class ResearchTask:
    task_id: str
    topic: str
    instructions: str
    assigned_worker: str
    status: str = "PENDING"
    raw_findings: List[str] = field(default_factory=list)
    citations: List[str] = field(default_factory=list)

@dataclass
class SwarmState:
    """Shared blackboard memory across the swarm."""
    objective: str
    tasks: List[ResearchTask] = field(default_factory=list)
    critic_feedback: List[str] = field(default_factory=list)
    final_report: Optional[str] = None
