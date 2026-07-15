import requests

EVCC_MODE_OFF = "off"
EVCC_MODE_PV = "pv"

class EvccApi:
    """
    Minimal wrapper around the evcc REST API.
    """

    def __init__(self, base_url="http://192.168.0.217:7070"):
        self.base_url = base_url.rstrip("/")

    def set_mode(self, loadpoint: int, mode: str):

        url = f"{self.base_url}/api/loadpoints/{loadpoint}/mode/{mode}"

        response = requests.post(url, timeout=5)

        response.raise_for_status()

        return response.json()
