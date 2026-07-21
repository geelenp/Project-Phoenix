"""
Project Phoenix

Execution plan.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Plan:
    """
    Execution plan produced by the planner.
    """

    actions: list = field(default_factory=list)
