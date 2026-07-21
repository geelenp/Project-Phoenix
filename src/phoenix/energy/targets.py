"""
Project Phoenix

Calculate energy targets.
"""


def create_targets(state, context):
    """
    Calculate target values for the planner.

    These targets are policy decisions.
    They do not directly control devices.
    """

    targets = {
        "grid_target_soc": 60,
        "ev_target": None,
        "boiler_target": None,
        "export_target": None,
    }

    return targets
