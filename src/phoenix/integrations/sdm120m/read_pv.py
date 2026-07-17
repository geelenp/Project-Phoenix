from datetime import UTC, datetime

import minimalmodbus

from config import PORT, SLAVE_ID, BAUDRATE

#
# SDM120M
#

instrument = minimalmodbus.Instrument(PORT, SLAVE_ID)

instrument.serial.baudrate = BAUDRATE
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1

#
# Registers
#

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

#
# Phoenix object
#

pv = {
    "generated": datetime.now(UTC),
    "power_kw": power / 1000.0,
    "voltage_v": voltage,
    "current_a": current,
    "energy_total_kwh": energy,
}

#
# Test output
#

print()
print("PV")
print()

print(f"Power    : {pv['power_kw']:.3f} kW")
print(f"Voltage  : {pv['voltage_v']:.1f} V")
print(f"Current  : {pv['current_a']:.2f} A")
print(f"Energy   : {pv['energy_total_kwh']:.1f} kWh")
