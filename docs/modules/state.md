## Benaming: state.py

## Korte beschrijving

Initialiseert de centrale Energy State van Project Phoenix.
De Energy State is de gedeelde gegevensstructuur waarin alle actuele informatie over de installatie wordt opgeslagen. Iedere reader werkt uitsluitend zijn eigen onderdeel van deze structuur bij.
state.py bepaalt uitsluitend de structuur van de Energy State en bevat geen berekeningen of beslissingslogica

## Ontvangt

Niets

## Levert

Een dictionary waarin voor iedere energiebron of component een plaats is gereserveerd (energy state)

## Wordt aangeroepen door

Main.py

## Roept aan

Niets

## Afhankelijkheden

geen

## Belangrijkste beleidsregels

Initialiseert de Energy State exact éénmaal bij het opstarten.
Definieert uitsluitend de structuur van de Energy State.
Bevat geen energielogica.
Bevat geen berekeningen.
Bevat geen plannerlogica.
Bevat geen apparaatlogica.
Iedere reader schrijft uitsluitend naar zijn eigen onderdeel van de Energy State.
Niet beschikbare gegevens worden geïnitialiseerd met None.
De structuur van de Energy State blijft gedurende de volledige uitvoering van Phoenix onveranderd.
Nieuwe apparaten worden toegevoegd door de structuur uit te breiden, zonder bestaande onderdelen te wijzigen.
De Energy State vormt de enige bron van actuele systeeminformatie voor de rest van Project Phoenix.

## Code

"""
Project Phoenix

Energy State.
"""

def create_state():
    """
    Create an empty Energy State.

    The Adapter Manager populates this state with the latest
    successful measurements from each reader.
    """

    return {}
