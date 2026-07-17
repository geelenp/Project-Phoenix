from datetime import UTC, datetime

from client import SBSClient


client = SBSClient()

print("Connecting...")

if not client.connect():
    print("Unable to connect to SBS.")
    exit()

try:

    battery = {

        "generated": datetime.now(UTC),

        "soc": client.read_u32(30845),

        "power_kw": client.read_s32(30775) / 1000.0,

        "current_a": client.read_s32(30843),

        "voltage_v": client.read_u32(30851) / 100.0,

    }

finally:

    client.close()


print()
print("Battery")
print()

print(f"SoC       : {battery['soc']} %")
print(f"Power     : {battery['power_kw']:.3f} kW")
print(f"Current   : {battery['current_a']} A")
print(f"Voltage   : {battery['voltage_v']:.2f} V")
