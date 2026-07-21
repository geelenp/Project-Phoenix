# Benaming: plan.py

## Korte beschrijving

Definieert de Plan-structuur die door de planner wordt gemaakt en door de executor wordt uitgevoerd.
Een Plan beschrijft welke acties uitgevoerd moeten worden om de gewenste energiedoelen te bereiken. Het bevat geen beslissingslogica en geen apparaatcommunicatie.
Het Plan vormt de scheiding tussen besluitvorming (planner.py) en uitvoering (executor.py).

## Ontvangt

Niets

## Levert

Plan

## Wordt aangeroepen door

planner.py
executor.py

## Roept aan

Niets

## Afhankelijkheden

Dataclasses

## Belangrijkste beleidsregels

Definieert uitsluitend de structuur van een Plan.
Bevat geen beslissingslogica.
Bevat geen apparaatlogica.
Bevat geen hardwareaansturing.
Een Plan beschrijft wat uitgevoerd moet worden.
Een Plan beschrijft niet hoe een apparaat moet worden aangestuurd.
De planner creëert een Plan.
De executor interpreteert en voert een Plan uit.
Het Plan is generiek en onafhankelijk van specifieke apparaten.
Nieuwe acties kunnen aan het Plan worden toegevoegd zonder de scheiding tussen planner en executor te doorbreken.

## Code

"""
Project Phoenix

Execution plan.
"""

from dataclasses import dataclass, field

@dataclass(slots=True)
class Plan:
    """
    Execution plan produced by the planner.
    """

    actions: list = field(default_factory=list)
