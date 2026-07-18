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

    battery_soc = status["battery_soc"]
    vehicle_soc = status["vehicle_soc"]

    return {
        "surplus": power["grid_export"] > 0,
        "importing": power["grid_import"] > 0,
        "battery_charging": power["battery_charge"] > 0,
        "battery_discharging": power["battery_discharge"] > 0,
        "vehicle_connected": status["vehicle_connected"],
        "vehicle_charging": status["vehicle_charging"],
        "battery_low": battery_soc < 10,
        "battery_full": battery_soc >= 95,
        "vehicle_low": vehicle_soc < 20,
        "vehicle_full": vehicle_soc >= 100,
    }
