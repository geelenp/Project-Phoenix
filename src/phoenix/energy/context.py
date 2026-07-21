"""
Project Phoenix

Build the Decision Context from the Energy State.
"""


def create_context(state):
    """
    Create the Decision Context.

    The Decision Context contains information that is useful for
    decision making, derived from the Energy State.
    """

    power = state["power"]
    status = state["status"]

    return {
        "surplus": power["grid_export"] > 0,
        "importing": power["grid_import"] > 0,
        "battery_charging": power["battery_charge"] > 0,
        "battery_discharging": power["battery_discharge"] > 0,
        "vehicle_connected": status["vehicle_connected"],
        "vehicle_charging": status["vehicle_charging"],
    }
