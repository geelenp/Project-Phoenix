# Benaming: planner.py

## Korte beschrijving

Bepaalt op basis van de actuele toestand en de gewenste doelen welk Plan moet worden uitgevoerd.
De planner is het besluitvormende onderdeel van Project Phoenix. Hij vergelijkt de actuele situatie met de gewenste situatie en stelt een plan op, zonder zich bezig te houden met de uitvoering daarvan.
De planner bevat uitsluitend beslissingslogica.

## Ontvangt

Energy state
Decision context
targets

## Levert

Plan

## Wordt aangeroepen door

Main.py
Via: create_plan(state, context, targets)

## Roept aan

Niets

## Afhankelijkheden

energy state

## Belangrijkste beleidsregels

Bevat uitsluitend beslissingslogica.
Voert zelf geen hardwareaansturing uit.
Bevat geen apparaatcommunicatie.
Werkt uitsluitend met de Energy State, Decision Context en Targets.
Produceert altijd een Plan als resultaat.
Beschrijft wat moet gebeuren, niet hoe dit wordt uitgevoerd.
De planner kent geen implementatiedetails van actuators of apparaten.
Beslissingen zijn volledig reproduceerbaar voor dezelfde invoer.
Nieuwe apparaten of energiedoelen kunnen worden ondersteund zonder de architectuur van de planner te wijzigen.
De uitvoering van het Plan is volledig de verantwoordelijkheid van executor.py.

## Code

"""
Project Phoenix

Create an execution plan from the Decision Context.
"""

def create_plan(state, context, targets):
    """
    Create an execution plan.

    The planner decides what should happen based on the
    current Energy State and Decision Context.
    """

    plan = []

    if not context["vehicle_connected"]:
        plan.append(
            {
                "target": "charger",
                "action": "set_power",
                "value": 0,
                "reason": "vehicle_not_connected",
            }
        )

    elif context["vehicle_charging"]:
        plan.append(
            {
                "target": "charger",
                "action": "keep_power",
                "reason": "vehicle_charging",
            }
        )

    return plan
