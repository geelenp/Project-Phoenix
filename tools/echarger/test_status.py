from status import read_status


data = read_status()

if data is None:
    print("Connection failed.")
    exit()

print()
print("========== SMA eCharger ==========\n")

for key, value in data.items():
    print(f"{key:15s}: {value}")
