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


def main():

    state = create_state()

    adapters = AdapterManager()

    while True:

        state = adapters.update(state)

        state = calculate(state)

        context = create_context(state)

        plan = create_plan(state, context)

        pprint(state)
        pprint(context)
        pprint(plan)

        sleep(1)


if __name__ == "__main__":
    main()
