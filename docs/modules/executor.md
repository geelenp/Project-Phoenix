# Benaming: executor.py

## Korte beschrijving

Voert het door de planner gemaakte Plan uit.
De executor vertaalt de generieke acties uit het Plan naar concrete aanroepen van de juiste actuators. Hij neemt zelf geen beslissingen en bepaalt niet welk plan uitgevoerd moet worden.
De executor vormt de schakel tussen besluitvorming en hardwareaansturing.

## Ontvangt

Plan

## Levert

Niets 
(De uitvoering vindt plaats via de actuators.)

## Wordt aangeroepen door

main.py

## Roept aan

actuators

## Afhankelijkheden

plan.py 
Actuator-modules

## Belangrijkste beleidsregels

Voert uitsluitend een Plan uit.
Bevat geen beslissingslogica.
Bevat geen energielogica.
Wijzigt het Plan niet.
Vertaalt generieke acties naar concrete actuator-aanroepen.
Kent de beschikbare actuators, maar niet de interne werking van de apparaten.
Iedere actuator is verantwoordelijk voor één apparaat of systeem.
De executor bepaalt niet of een actie wenselijk is; dat is uitsluitend de verantwoordelijkheid van de planner.
Nieuwe actuators kunnen worden toegevoegd zonder de architectuur van de executor te wijzigen.
De executor vormt de enige laag die rechtstreeks met actuators communiceert.

## Code

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
