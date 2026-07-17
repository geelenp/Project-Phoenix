from client import SBSClient


client = SBSClient()

print("Connecting...")

if not client.connect():
    print("Unable to connect.")
    exit()

print("Connected.")
print()

print("Battery")
print("-------")

print(f"SoC      : {client.read_u32(30845)} %")
print(f"Power    : {client.read_s32(30775)} W")
print(f"Current  : {client.read_s32(30843)}")
print(f"Voltage  : {client.read_u32(30851)}")

client.close()
