from pymodbus.client import ModbusTcpClient

from config import HOST, PORT, UNIT


client = ModbusTcpClient(
    host=HOST,
    port=PORT,
)

print("Connecting...")

if not client.connect():
    print("Unable to connect.")
    exit()

print("Connected.")

#
# Test register
#

result = client.read_holding_registers(
    address=50,
    count=2,
    device_id=UNIT,
)

print(result)

client.close()
