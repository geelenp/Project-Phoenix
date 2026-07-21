## Benaming: calculate.py

## Korte beschrijving

Verrijkt de Energy State met afgeleide gegevens.
Op basis van de actuele metingen worden grootheden berekend die niet rechtstreeks door een reader worden geleverd, maar wel door de rest van Phoenix worden gebruikt.
Het bestand bevat uitsluitend berekeningen en geen beslissingslogica.

## Ontvangt

Energy state

## Levert

Energy state aangevuld met berekende waarden

## Wordt aangeroepen door

Main.py

## Roept aan

Niets

## Afhankelijkheden

energy state

## Belangrijkste beleidsregels

Voert uitsluitend berekeningen uit.
Bevat geen plannerlogica.
Bevat geen apparaatlogica.
Bevat geen sturing van hardware.
Werkt uitsluitend met gegevens uit de Energy State.
Voegt uitsluitend afgeleide waarden toe aan de Energy State.
Overschrijft geen ruwe meetgegevens van readers.
Ontbrekende gegevens (None) worden veilig afgehandeld; berekeningen mogen hierdoor niet vastlopen.
Iedere berekening is onafhankelijk en heeft geen bijwerkingen buiten de Energy State.
Alle verdere onderdelen van Phoenix gebruiken deze berekende waarden in plaats van dezelfde berekeningen opnieuw uit te voeren.

## Code

"""
Project Phoenix

Calculate derived energy values.
"""

def calculate(state):
    """
    Calculate derived values from the current Energy State.
    """

    power = {}

    power["grid_w"] = state.get("grid", {}).get("power_w")
    power["pv_w"] = state.get("pv", {}).get("power_w")
    power["battery_w"] = state.get("battery", {}).get("power_w")
    power["charger_w"] = state.get("charger", {}).get("power_w")

    state["power"] = power

    return state
