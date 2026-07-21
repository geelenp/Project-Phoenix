"""
Project Phoenix

Create an execution plan from the Decision Context.
"""


def create_plan(state, context, targets):
    """
    Create an execution plan.

    The planner decides what should happen based on the
    current Energy State and Decision Context.
    """

    plan = []

    if not context["vehicle_connected"]:
        plan.append(
            {
                "target": "charger",
                "action": "set_power",
                "value": 0,
                "reason": "vehicle_not_connected",
            }
        )

    elif context["vehicle_charging"]:
        plan.append(
            {
                "target": "charger",
                "action": "keep_power",
                "reason": "vehicle_charging",
            }
        )

    return plan
