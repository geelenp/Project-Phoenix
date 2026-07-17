"""
Project Phoenix
Energy State

Single source of truth for the entire EMS.
"""


def create_state():
    """
    Create an empty Energy State.
    """

    return {

        #
        # Measurements
        #

        "grid": None,
        "battery": None,
        "charger": None,
        "vehicle": None,
        "pv": None,

        #
        # External data
        #

        "forecast": None,
        "prices": None,
    }
