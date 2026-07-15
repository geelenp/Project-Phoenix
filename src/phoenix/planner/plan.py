from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Plan:
    """
    Decision produced by the planner.
    """

    charge: bool
    reason: str
