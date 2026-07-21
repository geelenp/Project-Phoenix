# Benaming: rest.py

## Korte beschrijving

Stelt de gegevens van Project Phoenix beschikbaar via een REST API.
De REST-module biedt externe applicaties toegang tot de actuele toestand van het energiesysteem. De API is bedoeld voor integraties, dashboards en diagnostische toepassingen en maakt geen deel uit van de interne besluitvorming.

## Ontvangt

Energy State
Decision Context
Plan

## Levert
REST-responses.

## Wordt aangeroepen door

REST-server.

## Roept aan

Niets

## Afhankelijkheden

REST-framework.

## Belangrijkste beleidsregels

Stelt uitsluitend gegevens beschikbaar.
Bevat geen energielogica.
Bevat geen plannerlogica.
Stuurt geen apparaten aan.
Wijzigt de Energy State niet.
Is bedoeld voor externe applicaties, dashboards en diagnostische tools.
Een fout in de REST-interface mag de werking van Project Phoenix niet beïnvloeden.
De REST API is een optionele uitvoerlaag.

## Code

Nog te ontwikkelen