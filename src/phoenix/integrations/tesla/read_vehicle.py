import json
import requests

BASE_URL = "https://fleet-api.prd.eu.vn.cloud.tesla.com/api/1"

def wake_up(vehicle_id):

    print("Waking up vehicle...")

    response = requests.post(
        f"{BASE_URL}/vehicles/{vehicle_id}/wake_up",
        headers=headers,
        timeout=30,
    )

    print("Wake-up status:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        return False

    return True

#
# Access token laden
#

with open("tools/tesla/tokens.json") as f:
    tokens = json.load(f)

access_token = tokens["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}",
}

#
# Voertuigen ophalen
#

response = requests.get(
    f"{BASE_URL}/vehicles",
    headers=headers,
    timeout=30,
)

response.raise_for_status()

vehicles = response.json()["response"]

vehicle = vehicles[0]

vehicle_id = vehicle["id"]

print("Vehicle ID :", vehicle_id)
print("Name       :", vehicle["display_name"])
print("State      :", vehicle["state"])
print()

#
# Vehicle data ophalen
#

if vehicle["state"] != "online":

    if not wake_up(vehicle_id):
        exit(1)

    import time

    print("Waiting 10 seconds...")

    time.sleep(10)

response = requests.get(
    f"{BASE_URL}/vehicles/{vehicle_id}/vehicle_data",
    headers=headers,
    timeout=30,
)

response.raise_for_status()

data = response.json()["response"]

connected = data["state"] == "online"

charging = (
    data["charge_state"]["charging_state"] == "Charging"
)

soc = data["charge_state"]["battery_level"]

charge_limit = data["charge_state"]["charge_limit_soc"]

#
# Tesla geeft battery_range blijkbaar in miles
#

range_km = round(
    data["charge_state"]["battery_range"] * 1.60934
)

tesla = {
    "connected": connected,
    "charging": charging,
    "soc": soc,
    "charge_limit": charge_limit,
    "range_km": range_km,
}

print()
print("Tesla")
print()

print(f"Connected   : {tesla['connected']}")
print(f"Charging    : {tesla['charging']}")
print(f"SOC         : {tesla['soc']} %")
print(f"Limit       : {tesla['charge_limit']} %")
print(f"Range       : {tesla['range_km']} km")
