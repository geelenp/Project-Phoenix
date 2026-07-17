"""
Project Phoenix

Main entry point.
"""

from pprint import pprint

from phoenix.energy.state import create_state
from phoenix.energy.calculate import calculate


def main():
    """
    Phoenix main program.
    """

    state = create_state()

    #
    # Readers komen hier
    #

    state = calculate(state)

    pprint(state)


if __name__ == "__main__":
    main()
