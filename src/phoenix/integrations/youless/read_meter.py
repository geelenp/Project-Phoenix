from datetime import UTC, datetime

import requests

from config import HOST

URL = f"http://{HOST}/e"

response = requests.get(
    URL,
    timeout=10,
)

print("Status:", response.status_code)
print()

response.raise_for_status()

data = response.json()[0]
print(data)
print()

#
# Phoenix object
#

grid = {
    "generated": datetime.now(UTC),

    "power_kw": data["pwr"] / 1000.0,

    "energy_import_kwh": data["p1"] + data["p2"],

    "energy_export_kwh": data["n1"] + data["n2"],

    "gas_m3": data["gas"],

    "raw": data,
}

#
# Test output
#

print("Grid")
print()

print(f"Power      : {grid['power_kw']:.3f} kW")
print(f"Import     : {grid['energy_import_kwh']:.3f} kWh")
print(f"Export     : {grid['energy_export_kwh']:.3f} kWh")
print(f"Gas        : {grid['gas_m3']:.3f} m³")

