"""
Solcast test utility.

Reads the Solcast forecast and converts it to the Phoenix data structure.
"""

from datetime import UTC, datetime

import requests

from config import API_KEY, SITE_ID

URL = f"https://api.solcast.com.au/rooftop_sites/{SITE_ID}/forecasts"

response = requests.get(
    URL,
    params={
        "format": "json",
    },
    headers={
        "Authorization": f"Bearer {API_KEY}",
    },
    timeout=30,
)

response.raise_for_status()

raw = response.json()

solcast = {
    "generated": datetime.now(UTC),
    "forecast": [],
}

for item in raw["forecasts"]:

    solcast["forecast"].append(
        {
            "time": datetime.fromisoformat(
                item["period_end"].replace("Z", "+00:00")
            ),
            "pv_kw": float(item["pv_estimate"]),
        }
    )

print()
print("Solcast")
print()

for forecast in solcast["forecast"][:10]:

    print(
        forecast["time"].strftime("%Y-%m-%d %H:%M UTC"),
        "->",
        f"{forecast['pv_kw']:.2f} kW",
    )
