"""
Project Phoenix

Calculate derived energy values.
"""


def calculate(state):
    """
    Calculate derived values from the current Energy State.
    """

    power = {}

    power["grid_w"] = state.get("grid", {}).get("power_w")
    power["pv_w"] = state.get("pv", {}).get("power_w")
    power["battery_w"] = state.get("battery", {}).get("power_w")
    power["charger_w"] = state.get("charger", {}).get("power_w")

    state["power"] = power

    return state
