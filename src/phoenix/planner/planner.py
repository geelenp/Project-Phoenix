"""
Project Phoenix

Planner.
"""

from phoenix.planner.plan import Plan


class Planner:
    """
    Phoenix EMS planner.
    """

    def create_plan(self, state, context, targets) -> Plan:
        """
        Build an execution plan from the current state,
        decision context and policy targets.
        """

        plan = Plan()

        #
        # Battery planning
        #

        #
        # EV planning
        #

        #
        # Boiler planning
        #

        return plan
