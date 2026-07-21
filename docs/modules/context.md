## Benaming: context.py

## Korte beschrijving

Maakt op basis van de Energy State een Decision Context.
De Decision Context bevat uitsluitend feitelijke informatie die relevant is voor besluitvorming. Deze informatie wordt afgeleid uit de actuele toestand van het energiesysteem en vormt de invoer voor de planner.
Het bestand bevat geen beleidsregels of beslissingen.

## Ontvangt

Energy state

## Levert

Decision context

## Wordt aangeroepen door

Main.py
Via: create_context(state)

## Roept aan

Niets

## Afhankelijkheden

energy state

## Belangrijkste beleidsregels

Bevat uitsluitend feitelijke afleidingen uit de Energy State.
Bevat geen plannerlogica.
Bevat geen apparaatlogica.
Bevat geen energiedoelen.
Bevat geen beleidsregels.
Levert uitsluitend informatie die op dit moment waar of onwaar is.
Iedere contextwaarde wordt onafhankelijk bepaald.
De Decision Context wordt bij iedere cyclus opnieuw opgebouwd.
De planner gebruikt uitsluitend de Decision Context voor feitelijke systeeminformatie.
Nieuwe contextwaarden kunnen worden toegevoegd zonder bestaande logica te wijzigen.

## Code

"""
Project Phoenix

Build the Decision Context from the Energy State.
"""

def create_context(state):
    """
    Create the Decision Context.

    The Decision Context contains information that is useful for
    decision making, derived from the Energy State.
    """

    power = state["power"]
    status = state["status"]

    return {
        "surplus": power["grid_export"] > 0,
        "importing": power["grid_import"] > 0,
        "battery_charging": power["battery_charge"] > 0,
        "battery_discharging": power["battery_discharge"] > 0,
        "vehicle_connected": status["vehicle_connected"],
        "vehicle_charging": status["vehicle_charging"],
    }
