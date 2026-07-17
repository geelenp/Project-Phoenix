from datetime import UTC, datetime

import minimalmodbus

from .config import PORT, SLAVE_ID, BAUDRATE


def read():
    """
    Read the current PV state from the SDM120M.
    """

    instrument = minimalmodbus.Instrument(PORT, SLAVE_ID)

    instrument.serial.baudrate = BAUDRATE
    instrument.serial.bytesize = 8
    instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 1

    voltage = instrument.read_float(
        registeraddress=0,
        functioncode=4,
    )

    current = instrument.read_float(
        registeraddress=6,
        functioncode=4,
    )

    #
    # Phoenix convention:
    # PV production is always positive.
    #

    power = -instrument.read_float(
        registeraddress=12,
        functioncode=4,
    )

    energy = instrument.read_float(
        registeraddress=342,
        functioncode=4,
    )

    return {
        "generated": datetime.now(UTC),
        "power_kw": power / 1000.0,
        "voltage_v": voltage,
        "current_a": current,
        "energy_total_kwh": energy,
    }
