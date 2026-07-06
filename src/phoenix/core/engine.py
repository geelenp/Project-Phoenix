from phoenix.core.state import PhoenixState
from phoenix.core.validator import PhoenixValidator


class PhoenixEngine:
    """
    Coordinates the Phoenix core.

    Responsibilities:
    - update PhoenixState
    - validate state
    - expose a stable state for future planner execution

    Planner, Forecast and Outputs will be added later.
    """

    def __init__(self):
        self.state = PhoenixState()
        self.validator = PhoenixValidator()

    def process(self, event: dict):
        if not event:
            return

        #
        # Ignore forecast updates for now
        #

        if any(key.startswith("forecast.") for key in event):
            return

        #
        # Ignore evcc log messages
        #

        if "log" in event:
            level = event["log"].get("level", "info").upper()
            message = event["log"].get("message", "")

            print(f"[{level}] {message}")
            return

        #
        # Update state
        #

        self.state.update(event)

        #
        # Validate
        #

        warnings = self.validator.validate(self.state)

        #
        # Temporary console output
        #

        print(
            f"Grid={self.state.grid_power} W | "
            f"Home={self.state.home_power} W | "
            f"PV={self.state.pv_power} W | "
            f"Battery={self.state.battery_soc}%"
        )

        for warning in warnings:
            print(f"WARNING: {warning}")
