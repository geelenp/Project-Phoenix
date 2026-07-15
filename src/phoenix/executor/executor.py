from phoenix.executor.evcc_api import (
    EvccApi,
    EVCC_MODE_OFF,
    EVCC_MODE_PV,
)
from phoenix.planner.plan import Plan


class Executor:
    """
    Executes a planner decision.
    """

    def __init__(self):
        self.evcc = EvccApi()
        self.last_mode = None

    def execute(self, plan: Plan):

        mode = EVCC_MODE_PV if plan.charge else EVCC_MODE_OFF

        #
        # Nothing changed
        #

        if mode == self.last_mode:
            return

        print(f"Executor : switching evcc to '{mode}'")

        self.evcc.set_mode(1, mode)

        self.last_mode = mode
