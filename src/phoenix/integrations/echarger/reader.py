"""
Project Phoenix

SMA eCharger reader.
"""

from datetime import UTC, datetime

from .client import EChargerClient
from . import registers as reg


def read():
    """
    Read the current charger state.
    """

    client = EChargerClient()

    if not client.connect():
        return None

    try:

        def read_register(register):
            try:
                return client.read(register)
            except Exception:
                return None

        data = {

            #
            # Metadata
            #

            "generated": datetime.now(UTC),

            #
            # Device information
            #

            "device_class": read_register(reg.DEVICE_CLASS),
            "device_type": read_register(reg.DEVICE_TYPE),
            "firmware": read_register(reg.FIRMWARE),

            #
            # Status
            #

            "status": read_register(reg.STATUS),
            "speedwire_status": read_register(reg.SPEEDWIRE_STATUS),

            #
            # Charger
            #

            "max_power": read_register(reg.MAX_POWER),

            #
            # Active power
            #

            "power_l1": read_register(reg.POWER_L1),
            "power_l2": read_register(reg.POWER_L2),
            "power_l3": read_register(reg.POWER_L3),

            #
            # Grid voltage
            #

            "voltage_l1": None,
            "voltage_l2": None,
            "voltage_l3": None,

            #
            # Reactive power
            #

            "reactive_total": read_register(reg.REACTIVE_TOTAL),
            "reactive_l1": read_register(reg.REACTIVE_L1),
            "reactive_l2": read_register(reg.REACTIVE_L2),
            "reactive_l3": read_register(reg.REACTIVE_L3),

            #
            # Apparent power
            #

            "apparent_total": read_register(reg.APPARENT_TOTAL),
            "apparent_l1": read_register(reg.APPARENT_L1),
            "apparent_l2": read_register(reg.APPARENT_L2),
            "apparent_l3": read_register(reg.APPARENT_L3),

            #
            # Total active power
            #

            "power_register": read_register(reg.TOTAL_ACTIVE_POWER),
        }

        value = read_register(reg.VOLTAGE_L1)
        if value is not None:
            data["voltage_l1"] = value / 100

        value = read_register(reg.VOLTAGE_L2)
        if value is not None:
            data["voltage_l2"] = value / 100

        value = read_register(reg.VOLTAGE_L3)
        if value is not None:
            data["voltage_l3"] = value / 100

        powers = [
            data["power_l1"],
            data["power_l2"],
            data["power_l3"],
        ]

        if None not in powers:
            power_calculated = sum(powers)
        else:
            power_calculated = None

        if data["power_register"] is not None:
            data["power"] = data["power_register"]
        else:
            data["power"] = power_calculated

        del data["power_register"]

        return data

    finally:
        client.close()
