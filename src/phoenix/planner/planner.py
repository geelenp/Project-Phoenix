from phoenix.planner.plan import Plan


class Planner:
    """
    Phoenix EMS planner.

    The planner is stateless.

    Input:
        PhoenixState

    Output:
        Plan
    """

    def create_plan(self, state):
        #
        # No EV connected
        #

        if not state.data.get("car", {}).get("connected", False):
            return Plan(
                mode="idle",
                reason="No EV connected",
                charge_power=0,
            )

        #
        # Fast charging requested
        #

        if state.data.get("car", {}).get("fast_requested", False):
            return Plan(
                mode="fast",
                reason="Fast charging requested",
                charge_power=99999,
            )

        #
        # Default
        #

        return Plan(
            mode="smart",
            reason="Normal EMS operation",
            charge_power=0,
        )
