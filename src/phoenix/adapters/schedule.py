"""
Project Phoenix

Reader schedule.
"""

from datetime import time


SCHEDULE = {

    # Fast
    "grid": {
        "interval": 15,
    },

    "charger": {
        "interval": 30,
    },

    "pv": {
        "interval": 30,
    },

    # Slow
    "battery": {
        "interval": 300,
    },

    "vehicle": {
        "interval": 600,
    },

    # Scheduled
    "forecast": {
        "times": [
            time(6, 0),
            time(11, 0),
            time(16, 0),
        ],
    },

    "prices": {
        "times": [
            time(15, 0),
        ],
    },
}
