from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class DecisionContext:
    """
    Immutable snapshot used by the planner.

    The planner never reads PhoenixState directly.
    """

    car_connected: bool
    car_charging: bool

    grid_power: float | None
    pv_power: float | None

    battery_soc: int | None
