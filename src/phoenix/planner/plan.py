from dataclasses import dataclass


@dataclass(slots=True)
class Plan:
    """
    Result produced by the Phoenix Planner.
    """

    mode: str = "idle"
    reason: str = ""
    charge_power: int = 0
