import requests


class TeslaClient:
    """
    Minimal Tesla Fleet API client.

    At this stage the client only performs
    authenticated GET requests.
    """

    def __init__(self, access_token: str):

        self.access_token = access_token

        self.base_url = "https://fleet-api.prd.eu.vn.cloud.tesla.com/api/1"

    def get(self, endpoint: str):

        response = requests.get(
            f"{self.base_url}/{endpoint}",
            headers={
                "Authorization": f"Bearer {self.access_token}"
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()
