## Benaming: schedule.py

## Korte beschrijving

Definieert de uitvoeringsplanning van alle readers binnen Project Phoenix.
schedule.py bevat uitsluitend de configuratie die bepaalt wanneer een reader uitgevoerd moet worden. De daadwerkelijke uitvoering gebeurt door AdapterManager.
Het bestand bevat geen programmalogica; uitsluitend planning

## Ontvangt

Niets

## Levert

Een configuratie-object dat voor iedere reader de uitvoeringsfrequentie of geplande tijdstippen beschrijft (schedule)

## Wordt aangeroepen door

Manager.py

## Roept aan

Niets

## Afhankelijkheden

datetime.time

## Belangrijkste beleidsregels

Bevat uitsluitend configuratie.
Bevat geen programmalogica.
Bevat geen energielogica.
Bevat geen apparaatlogica.
Iedere reader heeft precies één planning.
Een reader gebruikt óf een interval óf vaste tijdstippen, nooit beide.
Bij het opstarten wordt deze planning genegeerd; alle readers worden één keer uitgevoerd door AdapterManager.
Daarna bepaalt uitsluitend deze planning wanneer een reader opnieuw wordt uitgevoerd.
Er bestaat bewust geen retry-mechanisme. Mislukte reads worden automatisch opnieuw geprobeerd bij de volgende geplande uitvoering.
De gekozen intervallen zijn gebaseerd op de verwachte wijzigingssnelheid van de gegevensbron, niet op de pollingmogelijkheden van het apparaat.

## Code

"""
Project Phoenix

Reader schedule.
"""

from datetime import time

SCHEDULE = {

    # Fast
    "grid": {
        "interval": 15,
    },

    "charger": {
        "interval": 30,
    },

    "pv": {
        "interval": 30,
    },

    # Slow
    "battery": {
        "interval": 300,
    },

    "vehicle": {
        "interval": 600,
    },

    # Scheduled
    "forecast": {
        "times": [
            time(6, 0),
            time(11, 0),
            time(16, 0),
        ],
    },

    "prices": {
        "times": [
            time(15, 0),
        ],
    },
}
