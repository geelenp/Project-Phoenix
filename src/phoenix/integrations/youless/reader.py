from datetime import UTC, datetime

import requests

from .config import HOST


URL = f"http://{HOST}/e"


def read():
    """
    Read the current grid state from the Youless meter.
    """

    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    data = response.json()[0]

    return {
        "generated": datetime.now(UTC),
        "power": data["pwr"],
        "energy_import_kwh": data["p1"] + data["p2"],
        "energy_export_kwh": data["n1"] + data["n2"],
        "gas_m3": data["gas"],
        "raw": data,
    }
