"""
Project Phoenix

Tesla vehicle reader.
"""

from datetime import UTC, datetime
import time

from .client import TeslaClient


def read():

    client = TeslaClient()

    #
    # Vehicle list
    #

    vehicles = client.get("vehicles")

    vehicle = vehicles["response"][0]
    vehicle_id = vehicle["id"]

    #
    # Wake up if necessary
    #

    if vehicle["state"] != "online":

        client.post(
            f"vehicles/{vehicle_id}/wake_up"
        )

        time.sleep(10)

    #
    # Vehicle data
    #

    data = client.get(
        f"vehicles/{vehicle_id}/vehicle_data"
    )["response"]

    return {
        "generated": datetime.now(UTC),
        "connected": data["state"] == "online",
        "charging": (
            data["charge_state"]["charging_state"] == "Charging"
        ),
        "soc": data["charge_state"]["battery_level"],
        "charge_limit": data["charge_state"]["charge_limit_soc"],
        "range_km": round(
            data["charge_state"]["battery_range"] * 1.60934
        ),
        "raw": data,
    }
