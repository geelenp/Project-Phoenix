"""
Project Phoenix
SMA eCharger reader
"""

from client import EChargerClient
import registers as reg


def read_echarger():

    client = EChargerClient()

    if not client.connect():
        return None

    def read(register):
        try:
            return client.read(register)
        except Exception:
            return None

    data = {

        #
        # Device information
        #

        "device_class": read(reg.DEVICE_CLASS),
        "device_type": read(reg.DEVICE_TYPE),
        "firmware": read(reg.FIRMWARE),

        #
        # Status
        #

        "status": read(reg.STATUS),
        "speedwire_status": read(reg.SPEEDWIRE_STATUS),

        #
        # Charger
        #

        "max_power": read(reg.MAX_POWER),

        #
        # Active Power
        #

        "power_l1": read(reg.POWER_L1),
        "power_l2": read(reg.POWER_L2),
        "power_l3": read(reg.POWER_L3),

        #
        # Grid Voltage (FIX2)
        #

        "voltage_l1": None,
        "voltage_l2": None,
        "voltage_l3": None,

        #
        # Reactive Power
        #

        "reactive_total": read(reg.REACTIVE_TOTAL),
        "reactive_l1": read(reg.REACTIVE_L1),
        "reactive_l2": read(reg.REACTIVE_L2),
        "reactive_l3": read(reg.REACTIVE_L3),

        #
        # Apparent Power
        #

        "apparent_total": read(reg.APPARENT_TOTAL),
        "apparent_l1": read(reg.APPARENT_L1),
        "apparent_l2": read(reg.APPARENT_L2),
        "apparent_l3": read(reg.APPARENT_L3),

        #
        # Total Active Power (register 35457)
        #

        "power_total_register": read(reg.TOTAL_ACTIVE_POWER),

    }

    #
    # Convert voltages (FIX2)
    #

    value = read(reg.VOLTAGE_L1)
    if value is not None:
        data["voltage_l1"] = value / 100

    value = read(reg.VOLTAGE_L2)
    if value is not None:
        data["voltage_l2"] = value / 100

    value = read(reg.VOLTAGE_L3)
    if value is not None:
        data["voltage_l3"] = value / 100

    #
    # Calculate total power
    #

    powers = [
        data["power_l1"],
        data["power_l2"],
        data["power_l3"],
    ]

    if None not in powers:
        data["power_total_calculated"] = sum(powers)
    else:
        data["power_total_calculated"] = None

    #
    # Preferred total power
    #

    if data["power_total_register"] is not None:
        data["power_total"] = data["power_total_register"]
    else:
        data["power_total"] = data["power_total_calculated"]

    #
    # Internal helper fields no longer needed
    #

    del data["power_total_register"]
    del data["power_total_calculated"]

    client.close()

    return data


if __name__ == "__main__":

    from pprint import pprint

    pprint(read_echarger())
