"""
Project Phoenix

Tesla Fleet API client.
"""

import requests

from .auth import get_access_token
from .config import BASE_URL


class TeslaClient:

    def __init__(self):

        self.base_url = BASE_URL

    def get(self, endpoint: str):

        response = requests.get(
            f"{self.base_url}/{endpoint}",
            headers=self._headers(),
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint: str):

        response = requests.post(
            f"{self.base_url}/{endpoint}",
            headers=self._headers(),
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def _headers(self):

        return {
            "Authorization": f"Bearer {get_access_token()}",
        }
