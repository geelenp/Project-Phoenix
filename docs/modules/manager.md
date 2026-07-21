## Benaming: manager.py

## Korte beschrijving

De AdapterManager beheert alle readers binnen Project Phoenix.
Hij bepaalt wanneer iedere reader uitgevoerd moet worden volgens de ingestelde planning en zorgt ervoor dat de opgehaalde gegevens in de centrale Energy State terechtkomen.
De manager kent geen inhoudelijke kennis van de apparaten; hij behandelt iedere reader identiek.

## Ontvangt

De huidige centrale Energy State (state)

## Levert

State

## Wordt aangeroepen door

main.py (via AdapterManager.update(state))

## Roept aan

Alle geregistreerde readers
Youless reader
SBS reader
eCharger reader
Tesla reader
SDM120M reader
Solcast reader
ENTSO-E reader

## Afhankelijkheden

Schedule.py

## Belangrijkste beleidsregels

Beheert uitsluitend wanneer readers worden uitgevoerd.
Kent geen energielogica.
Kent geen plannerlogica.
Kent geen apparatenpecifieke beslissingen.
Iedere reader wordt onafhankelijk behandeld.
Een fout in één reader mag de overige readers niet verhinderen om uitgevoerd te worden.
Bij het opstarten worden alle readers exact één keer uitgevoerd.
Daarna bepaalt uitsluitend schedule.py wanneer een reader opnieuw wordt uitgevoerd.
De tijd van de laatste poging wordt opgeslagen, ongeacht of de reader succesvol was.
Er bestaat bewust geen retry-mechanisme; periodieke of geplande updates zorgen vanzelf voor een volgende poging.
Readers schrijven uitsluitend hun eigen deel van de Energy State bij.
De manager creëert of verwijdert geen onderdelen van de Energy State.
De manager is volledig generiek: nieuwe readers kunnen worden toegevoegd zonder de manager zelf te wijzigen, behalve het registreren van de reader.

## Code 

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

        now = datetime.now()

        if "interval" in config:

            elapsed = (now - last_run).total_seconds()

            return elapsed >= config["interval"]

        if "times" in config:

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

        except Exception as e:
            print(f"FOUT {name}: {e}")

        finally:
            self.last_run[name] = datetime.now()
