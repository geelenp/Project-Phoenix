## Benaming: main.py
## Korte beschrijving

Het hoofdprogramma van Project Phoenix.
main.py initialiseert het systeem, creëert de globale Energy State en start de hoofdloop. Tijdens iedere cyclus worden achtereenvolgens de actuele gegevens opgehaald, de energietoestand berekend, de besliscontext opgebouwd, de beleidsdoelen bepaald en een uitvoeringsplan samengesteld.
main.py bevat geen enkele energielogica. Het coördineert uitsluitend de verschillende onderdelen van het systeem.

## Ontvangt

Niets.
Program wordt rechtstreeks gestart door Python.

## Levert

Niets
main.py vormt startpunt van volledige EMS-pijplijn.

## Wordt aangeroepen door

Python interpreter
Python main.py

## Roept aan

create_state()
AdapterManager.update()
calculate()
create_context()
create_targets()
create_plan()

## Afhankelijkheden

pprint
time.sleep
phoenix.adapters.manager
phoenix.energy.state
phoenix.energy.calculate
phoenix.energy.context
phoenix.energy.targets
phoenix.energy.planner

## Belangrijkste beleidsregels

Initialiseert de Energy State exact éénmaal. 
Initialiseert de AdapterManager exact éénmaal. 
Kent geen enkele kennis over apparaten. 
Kent geen enkele energielogica. 
Kent geen beleidsregels. 
Beslist nooit zelf. 
Roept de EMS-pipeline steeds in dezelfde volgorde aan. 
Iedere stap ontvangt uitsluitend de output van de vorige stap. 
De hoofdloop blijft zo eenvoudig mogelijk

## Code 

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

