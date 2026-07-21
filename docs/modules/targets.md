## Benaming: targets.py

## Korte beschrijving

Bepaalt de gewenste toestand (Targets) van het energiesysteem.
Targets beschrijven wat Phoenix wil bereiken, onafhankelijk van hoe dat wordt uitgevoerd. Ze vormen de invoer voor de planner, die bepaalt welke acties nodig zijn om deze doelen te realiseren.
Het bestand bevat uitsluitend de gewenste eindtoestand en geen beslissings- of uitvoeringslogica.

## Ontvangt

Energy state

## Levert

Een verzameling gewenste doelwaarden voor het energiesysteem (targets)

## Wordt aangeroepen door

Main.py
Via: create_targets(state)

## Roept aan

Niets

## Afhankelijkheden

energy state

## Belangrijkste beleidsregels

Bevat uitsluitend energiedoelen.
Bevat geen plannerlogica.
Bevat geen apparaatlogica.
Bevat geen hardwareaansturing.
Beschrijft uitsluitend de gewenste eindtoestand.
Targets zijn onafhankelijk van de manier waarop ze worden gerealiseerd.
Niet ieder apparaat hoeft een target te hebben.
Export is bewust geen target; export ontstaat automatisch wanneer aan alle andere energiedoelen is voldaan.
Nieuwe energiedoelen kunnen worden toegevoegd zonder de bestaande targets te wijzigen.
De planner gebruikt de Targets als gewenste situatie naast de actuele toestand uit de Decision Context.

## Code

"""
Project Phoenix

Calculate energy targets.
"""

def create_targets(state, context):
    """
    Calculate target values for the planner.

    These targets are policy decisions.
    They do not directly control devices.
    """

    targets = {
        "grid_target_soc": 60,
        "ev_target": None,
        "boiler_target": None,
        "export_target": None,
    }

    return targets
