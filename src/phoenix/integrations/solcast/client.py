"""
Project Phoenix

Solcast API client.
"""

import requests


class SolcastClient:

    def __init__(self, api_key: str, site_id: str):

        self.api_key = api_key
        self.site_id = site_id

    def forecasts(self):

        response = requests.get(
            f"https://api.solcast.com.au/rooftop_sites/{self.site_id}/forecasts",
            params={
                "format": "json",
            },
            headers={
                "Authorization": f"Bearer {self.api_key}",
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()
