from datetime import UTC, datetime

from .client import SBSClient


def read():
    """
    Read the current battery state from the SBS.
    """

    client = SBSClient()

    if not client.connect():
        raise ConnectionError("Unable to connect to SBS.")

    try:
        return {
            "generated": datetime.now(UTC),
            "soc": client.read_u32(30845),
            "power": client.read_s32(30775),
            "current": client.read_s32(30843),
            "voltage": client.read_u32(30851) / 100.0,
        }
    finally:
        client.close()
