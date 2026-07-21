"""
Project Phoenix

Derive values from the raw Energy State.
"""

from datetime import UTC, datetime


def value(device, key, default=None):
    """
    Safely retrieve a value from a device measurement.
    """

    if device is None:
        return default

    return device.get(key, default)


def calculate(state):
    """
    Enrich the Energy State with derived values.
    """

    grid = value(state["grid"], "power", 0)
    pv = value(state["pv"], "power", 0)
    battery = value(state["battery"], "power", 0)
    charger = value(state["charger"], "power", 0)

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
        "grid_import": value(state["grid"], "energy_import_kwh"),
        "grid_export": value(state["grid"], "energy_export_kwh"),
        "pv_total": value(state["pv"], "energy_total_kwh"),
    }

    state["status"] = {
        "battery_soc": value(state["battery"], "soc"),
        "vehicle_soc": value(state["vehicle"], "soc"),
        "vehicle_connected": value(state["vehicle"], "connected", False),
        "vehicle_charging": value(state["vehicle"], "charging", False),
    }

    now = datetime.now(UTC)

    state["timestamps"] = {
        "grid": value(state["grid"], "generated"),
        "battery": value(state["battery"], "generated"),
        "charger": value(state["charger"], "generated"),
        "vehicle": value(state["vehicle"], "generated"),
        "pv": value(state["pv"], "generated"),
        "calculated": now,
    }

    return state
