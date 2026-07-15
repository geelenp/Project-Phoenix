from phoenix.core.state import PhoenixState
from phoenix.executor.executor import Executor
from phoenix.planner.context import DecisionContext
from phoenix.planner.planner import Planner


class PhoenixEngine:
    """
    Central EMS engine.
    """

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()

    def run(self, state: PhoenixState):

        context = DecisionContext(
            car_connected=state.car_connected,
            car_charging=state.car_charging,
            grid_power=state.grid_power,
            pv_power=state.pv_power,
            battery_soc=state.battery_soc,
        )

        plan = self.planner.create_plan(context)

        self.executor.execute(plan)

        return plan
