from phoenix.planner.context import DecisionContext
from phoenix.planner.plan import Plan


class Planner:
    """
    Phoenix EMS planner.

    Stateless.
    Receives a DecisionContext.
    Returns a Plan.
    """

    def create_plan(self, context: DecisionContext) -> Plan:

        #
        # No EV connected
        #

        if not context.car_connected:
            return Plan(
                mode="idle",
                reason="No EV connected",
            )

        #
        # EV connected
        #

        return Plan(
            mode="smart",
            reason="EV connected",
        )
