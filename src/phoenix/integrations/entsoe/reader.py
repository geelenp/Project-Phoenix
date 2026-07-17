"""
Project Phoenix

ENTSO-E day-ahead price reader.
"""

from datetime import UTC, datetime, timedelta
import xml.etree.ElementTree as ET

from .client import EntsoeClient
from .config import API_KEY, DOMAIN


def read():

    client = EntsoeClient(API_KEY, DOMAIN)

    raw = client.prices()

    root = ET.fromstring(raw)

    ns = {
        "e": root.tag.split("}")[0].strip("{")
    }

    prices = []

    for series in root.findall("e:TimeSeries", ns):

        period = series.find("e:Period", ns)

        start = datetime.strptime(
            period.find(
                "e:timeInterval/e:start",
                ns,
            ).text,
            "%Y-%m-%dT%H:%MZ",
        ).replace(tzinfo=UTC)

        resolution = period.find(
            "e:resolution",
            ns,
        ).text

        if resolution == "PT15M":
            step = timedelta(minutes=15)

        elif resolution == "PT60M":
            step = timedelta(hours=1)

        else:
            raise ValueError(
                f"Unsupported resolution: {resolution}"
            )

        for point in period.findall(
            "e:Point",
            ns,
        ):

            position = int(
                point.find(
                    "e:position",
                    ns,
                ).text
            )

            price_eur_mwh = float(
                point.find(
                    "e:price.amount",
                    ns,
                ).text
            )

            prices.append(
                {
                    "time": start + (position - 1) * step,
                    "price_eur_kwh": price_eur_mwh / 1000.0,
                }
            )

    return {
        "generated": datetime.now(UTC),
        "prices": prices,
    }
