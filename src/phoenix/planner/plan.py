from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Plan:
    """
    Result produced by the Phoenix planner.
    """

    mode: str
    reason: str
