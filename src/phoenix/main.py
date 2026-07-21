"""
Project Phoenix
"""

from pprint import pprint
from time import sleep

from phoenix.adapters.manager import AdapterManager
from phoenix.energy.calculate import calculate
from phoenix.energy.context import create_context
from phoenix.energy.planner import create_plan
from phoenix.energy.state import create_state
from phoenix.energy.targets import create_targets


def main():

    state = create_state()

    adapters = AdapterManager()

    while True:

        state = adapters.update(state)

        state = calculate(state)

        context = create_context(state)

        targets = create_targets(state, context)

        plan = create_plan(state, context, targets)

        pprint(state)
        pprint(context)
        pprint(targets)
        pprint(plan)

        sleep(1)


if __name__ == "__main__":
    main()
