"""
Project Phoenix

Derive values from the raw Energy State.
"""

from datetime import UTC, datetime


def calculate(state):
    """
    Enrich the Energy State with derived values.
    """

    grid = state["grid"]["power"]
    pv = state["pv"]["power"]
    battery = state["battery"]["power"]
    charger = state["charger"]["power"]

    state["power"] = {
        "grid": grid,
        "grid_import": max(grid, 0),
        "grid_export": max(-grid, 0),
        "pv": pv,
        "battery": battery,
        "battery_charge": max(-battery, 0),
        "battery_discharge": max(battery, 0),
        "charger": charger,
        "house": grid + pv + battery - charger,
    }

    state["energy"] = {
        "grid_import": state["grid"]["energy_import_kwh"],
        "grid_export": state["grid"]["energy_export_kwh"],
        "pv_total": state["pv"]["energy_total_kwh"],
    }

    state["status"] = {
        "battery_soc": state["battery"]["soc"],
        "vehicle_soc": state["vehicle"]["soc"],
        "vehicle_connected": state["vehicle"]["connected"],
        "vehicle_charging": state["vehicle"]["charging"],
    }

    now = datetime.now(UTC)

    state["timestamps"] = {
        "grid": state["grid"]["generated"],
        "battery": state["battery"]["generated"],
        "charger": state["charger"]["generated"],
        "vehicle": state["vehicle"]["generated"],
        "pv": state["pv"]["generated"],
        "calculated": now,
    }

    return state
