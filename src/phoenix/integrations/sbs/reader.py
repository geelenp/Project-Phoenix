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
            "power_kw": client.read_s32(30775) / 1000.0,
            "current_a": client.read_s32(30843),
            "voltage_v": client.read_u32(30851) / 100.0,
        }
    finally:
        client.close()
