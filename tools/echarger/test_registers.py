import struct
import time

from pymodbus.client import ModbusTcpClient

from config import HOST, PORT, UNIT


START = 30051
END = 43101
STEP = 2


def decode(registers):

    r1, r2 = registers

    u32 = (r1 << 16) | r2

    s32 = u32
    if s32 >= 0x80000000:
        s32 -= 0x100000000

    raw = struct.pack(">HH", r1, r2)
    f32 = struct.unpack(">f", raw)[0]

    return u32, s32, f32


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

for register in range(START, END + 1, STEP):

    try:

        result = client.read_holding_registers(
            address=register,
            count=2,
            device_id=UNIT,
        )

        if result.isError():
            continue

        u32, s32, f32 = decode(result.registers)

        #
        # Officiële SMA NaN-waarden overslaan
        #

        if u32 == 0xFFFFFFFF:
            continue

        if u32 == 0x80000000:
            continue

        print(f"Register {register}")
        print(f"  Raw   : {result.registers}")
        print(f"  U32   : {u32}")
        print(f"  S32   : {s32}")
        print(f"  Float : {f32}")
        print()

    except Exception:
        pass

    time.sleep(0.05)

client.close()
