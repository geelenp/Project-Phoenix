# Benaming: reader.py

## Korte beschrijving

Leest gegevens uit één specifieke gegevensbron of één specifiek apparaat.
Een reader haalt actuele informatie op en retourneert deze aan AdapterManager, die de Energy State bijwerkt.
Een reader bevat uitsluitend logica voor het uitlezen van gegevens en geen berekeningen of beslissingslogica.

## Ontvangt

Niets

## Levert

Dictionary met actuele meetgegevens.

## Wordt aangeroepen door

manager.py

## Roept aan

De betreffende gegevensbron of het betreffende apparaat (youless, SBS, eCharger, Tesla API, SOLCAST, ENTSO-E, …)

## Afhankelijkheden

Apparaat- of API-specifieke libraries.

## Belangrijkste beleidsregels

Leest uitsluitend gegevens.
Bevat geen energielogica.
Bevat geen berekeningen.
Bevat geen plannerlogica.
Bevat geen hardwareaansturing.
Leest uitsluitend één gegevensbron of één apparaat uit.
Retourneert uitsluitend actuele gegevens.
Wijzigt de Energy State niet rechtstreeks.
Kent geen andere readers.
Kan onafhankelijk van andere readers worden ontwikkeld en getest.
Fouten blijven zoveel mogelijk beperkt tot deze reader.
De uitvoeringsfrequentie wordt uitsluitend bepaald door schedule.py; de reader kent zijn eigen planning niet.

## Code

Nog te ontwikkelen