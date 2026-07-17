from pymodbus.client import ModbusTcpClient

from config import HOST, PORT, UNIT


START = 30000
END = 32100
STEP = 2


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

alive = 0

for register in range(START, END + 1, STEP):

    try:

        result = client.read_holding_registers(
            address=register,
            count=2,
            device_id=UNIT,
        )

        if result.isError():
            continue

        r1 = result.registers[0]
        r2 = result.registers[1]

        value = (r1 << 16) | r2

        print(f"{register:5d} : {r1:5d} {r2:5d}   {value}")

        alive += 1

    except Exception:
        pass

client.close()

print()
print(f"{alive} registers replied.")
