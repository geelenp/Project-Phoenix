from datetime import UTC, datetime, timedelta
import xml.etree.ElementTree as ET

import requests

from config import API_KEY, DOMAIN

URL = "https://web-api.tp.entsoe.eu/api"

#
# Vandaag (UTC)
#

today = datetime.now(UTC).replace(
    hour=0,
    minute=0,
    second=0,
    microsecond=0,
)

tomorrow = today + timedelta(days=1)

period_start = today.strftime("%Y%m%d%H%M")
period_end = tomorrow.strftime("%Y%m%d%H%M")

#
# API call
#

response = requests.get(
    URL,
    params={
        "securityToken": API_KEY,
        "documentType": "A44",
        "in_Domain": DOMAIN,
        "out_Domain": DOMAIN,
        "periodStart": period_start,
        "periodEnd": period_end,
    },
    timeout=30,
)

print("Status:", response.status_code)

response.raise_for_status()

#
# XML parser
#

root = ET.fromstring(response.text)

#
# Namespace automatisch bepalen
#

ns = {
    "e": root.tag.split("}")[0].strip("{")
}

#
# Phoenix object
#

entsoe = {
    "generated": datetime.now(UTC),
    "prices": [],
}

#
# Alle tijdsreeksen verwerken
#

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

        entsoe["prices"].append(
            {
                "time": start + (position - 1) * step,
                "price_eur_kwh": price_eur_mwh / 1000.0,
            }
        )

#
# Test output
#

print()
print("ENTSO-E")
print()

for price in entsoe["prices"][:10]:

    print(
        price["time"].strftime("%Y-%m-%d %H:%M UTC"),
        "->",
        f"{price['price_eur_kwh']:.4f} €/kWh",
    )
