# Benaming: constraints.py

## Korte beschrijving

Bevat de randvoorwaarden (Constraints) waarbinnen de planner beslissingen mag nemen.
Constraints beschrijven de technische, functionele en veiligheidsgrenzen van het energiesysteem. Ze bepalen welke acties toegestaan zijn, onafhankelijk van de actuele situatie of de gewenste doelen.
Het bestand bevat uitsluitend beperkingen en geen beslissings- of uitvoeringslogica.

## Ontvangt

Niets

## Levert

Constraints

## Wordt aangeroepen door

planner.py

## Roept aan

Niets

## Afhankelijkheden

Niets

## Belangrijkste beleidsregels

Bevat uitsluitend randvoorwaarden.
Bevat geen plannerlogica.
Bevat geen apparaatlogica.
Bevat geen hardwareaansturing.
Beschrijft uitsluitend wat wel of niet is toegestaan.
Constraints zijn onafhankelijk van de actuele Energy State.
Constraints zijn onafhankelijk van de gewenste Targets.
De planner mag uitsluitend plannen genereren die binnen deze randvoorwaarden vallen.
Nieuwe beperkingen kunnen worden toegevoegd zonder de architectuur van de planner te wijzigen.
Alle veiligheids- en systeemgrenzen worden centraal beheerd in dit bestand.

## Code

Nog te ontwikkelen