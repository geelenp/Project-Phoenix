"""
Project Phoenix

Adapter Manager.
"""

from datetime import datetime

from phoenix.integrations.youless.reader import read as read_grid
from phoenix.integrations.sbs.reader import read as read_battery
from phoenix.integrations.echarger.reader import read as read_charger
from phoenix.integrations.tesla.reader import read as read_vehicle
from phoenix.integrations.sdm120m.reader import read as read_pv
from phoenix.integrations.solcast.reader import read as read_forecast
from phoenix.integrations.entsoe.reader import read as read_prices

from .schedule import SCHEDULE


class AdapterManager:

    def __init__(self):

        self.readers = {
            "grid": read_grid,
            "battery": read_battery,
            "charger": read_charger,
            "vehicle": read_vehicle,
            "pv": read_pv,
            "forecast": read_forecast,
            "prices": read_prices,
        }

        self.schedule = SCHEDULE

        self.last_run = {
            name: None
            for name in self.readers
        }

    def update(self, state):

        for name in self.readers:

            if self.is_due(name):
                self.update_reader(name, state)

        return state

    def is_due(self, name):

        config = self.schedule[name]
        last_run = self.last_run[name]

        if last_run is None:
            return True

        if "interval" in config:

            elapsed = (datetime.now() - last_run).total_seconds()

            return elapsed >= config["interval"]

        if "times" in config:

            now = datetime.now()

            for run_time in config["times"]:

                scheduled = now.replace(
                    hour=run_time.hour,
                    minute=run_time.minute,
                    second=0,
                    microsecond=0,
                )

                if last_run < scheduled <= now:
                    return True

            return False

        return False

    def update_reader(self, name, state):

        reader = self.readers[name]

        try:
            state[name] = reader()
            self.last_run[name] = datetime.now()

        except Exception as e:
            print(f"FOUT {name}: {e}")
