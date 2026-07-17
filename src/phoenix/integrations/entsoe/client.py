"""
Project Phoenix

ENTSO-E API client.
"""

from datetime import UTC, datetime, timedelta

import requests


class EntsoeClient:

    URL = "https://web-api.tp.entsoe.eu/api"

    def __init__(self, api_key: str, domain: str):

        self.api_key = api_key
        self.domain = domain

    def prices(self):

        today = datetime.now(UTC).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        tomorrow = today + timedelta(days=1)

        response = requests.get(
            self.URL,
            params={
                "securityToken": self.api_key,
                "documentType": "A44",
                "in_Domain": self.domain,
                "out_Domain": self.domain,
                "periodStart": today.strftime("%Y%m%d%H%M"),
                "periodEnd": tomorrow.strftime("%Y%m%d%H%M"),
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.text
