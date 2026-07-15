import minimalmodbus

from config import PORT, SLAVE_ID, BAUDRATE

#
# SDM120M Modbus instrument
#

instrument = minimalmodbus.Instrument(PORT, SLAVE_ID)

instrument.debug = True

instrument.serial.baudrate = BAUDRATE
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1

#
# Eastron SDM120M
# Register 30001 (offset 0)
# Voltage (Float32)
#

voltage = instrument.read_float(
    registeraddress=0,
    functioncode=4,
)

print()
print(f"Voltage : {voltage:.1f} V")
