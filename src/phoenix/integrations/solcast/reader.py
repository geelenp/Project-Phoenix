"""
Project Phoenix

Solcast forecast reader.
"""

from datetime import UTC, datetime

from .client import SolcastClient
from .config import API_KEY, SITE_ID


def read():

    client = SolcastClient(API_KEY, SITE_ID)

    raw = client.forecasts()

    forecast = []

    for item in raw["forecasts"]:

        forecast.append(
            {
                "time": datetime.fromisoformat(
                    item["period_end"].replace("Z", "+00:00")
                ),
                "pv_kw": float(item["pv_estimate"]),
            }
        )

    return {
        "generated": datetime.now(UTC),
        "forecast": forecast,
    }
