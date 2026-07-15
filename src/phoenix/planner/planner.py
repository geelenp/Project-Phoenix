from phoenix.planner.context import DecisionContext
from phoenix.planner.plan import Plan


class Planner:
    """
    Phoenix EMS planner.
    """

    def create_plan(self, context: DecisionContext) -> Plan:

        if not context.car_connected:
            return Plan(
                charge=False,
                reason="No EV connected",
            )

        if (context.grid_power or 0) < 0:
            return Plan(
                charge=True,
                reason="Grid export available",
            )

        return Plan(
            charge=False,
            reason="Waiting for surplus",
        )
