from pymodbus.client import ModbusTcpClient

from config import HOST, PORT, UNIT


REGISTERS = [30865, 30925]


client = ModbusTcpClient(
    host=HOST,
    port=PORT,
    timeout=2,
)

print(f"Connecting to {HOST}:{PORT}...")

if not client.connect():
    print("Connection failed.")
    exit()

print("Connected.\n")

for reg in REGISTERS:

    print(f"========== Register {reg} ==========")

    #
    # U16
    #
    try:
        result = client.read_holding_registers(
            address=reg,
            count=1,
            device_id=UNIT,
        )

        if result.isError():
            print("U16 : ERROR")
        else:
            print(f"U16 : {result.registers[0]}")

    except Exception as e:
        print(f"U16 : {e}")

    #
    # U32
    #
    try:
        result = client.read_holding_registers(
            address=reg,
            count=2,
            device_id=UNIT,
        )

        if result.isError():
            print("U32 : ERROR")
        else:
            r1, r2 = result.registers
            value = (r1 << 16) | r2
            print(f"U32 : [{r1}, {r2}] = {value}")

    except Exception as e:
        print(f"U32 : {e}")

    print()

client.close()
