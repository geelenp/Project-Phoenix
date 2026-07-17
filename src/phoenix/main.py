"""
Project Phoenix

Energy Management System
"""

from pprint import pprint

from phoenix.energy.calculate import calculate
from phoenix.energy.state import create_state

from phoenix.integrations.youless.reader import read as read_grid
from phoenix.integrations.sbs.reader import read as read_battery
from phoenix.integrations.echarger.reader import read as read_charger
from phoenix.integrations.tesla.reader import read as read_vehicle
from phoenix.integrations.sdm120m.reader import read as read_pv
from phoenix.integrations.solcast.reader import read as read_forecast
from phoenix.integrations.entsoe.reader import read as read_prices


def safe_read(name, reader):

    try:
        return reader()

    except Exception as e:

        print(f"{name}: {e}")

        return None


def main():

    state = create_state()

    state["grid"] = safe_read("Grid", read_grid)
    state["battery"] = safe_read("Battery", read_battery)
    state["charger"] = safe_read("Charger", read_charger)
    state["vehicle"] = safe_read("Tesla", read_vehicle)
    state["pv"] = safe_read("PV", read_pv)
    state["forecast"] = safe_read("Solcast", read_forecast)
    state["prices"] = safe_read("ENTSO-E", read_prices)

    state = calculate(state)

    print()
    pprint(state)
    print()


if __name__ == "__main__":
    main()
