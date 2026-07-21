# Benaming: logger.py

## Korte beschrijving

Legt gebeurtenissen en systeeminformatie van Project Phoenix vast.
De logger ondersteunt monitoring, foutanalyse en historiek, zonder invloed uit te oefenen op de werking van het energiesysteem.

## Ontvangt

Gebeurtenissen
Meldingen
Energy State
Plan

## Levert
Logbestanden of logberichten.

## Wordt aangeroepen door

Alle modules

## Roept aan

Logbestand of logging-systeem

## Afhankelijkheden

Python logging of een andere logging-library.

## Belangrijkste beleidsregels

Registreert uitsluitend informatie.
Bevat geen energielogica.
Bevat geen plannerlogica.
Stuurt geen apparaten aan.
Wijzigt geen gegevens binnen Phoenix.
Een fout in de logger mag de werking van Phoenix niet beïnvloeden.
Logging is een ondersteunende functie.

## Code

Nog te ontwikkelen