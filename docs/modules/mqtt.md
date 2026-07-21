# Benaming: mqtt.py

## Korte beschrijving

Maakt de gegevens van Project Phoenix beschikbaar via MQTT.
De MQTT-module publiceert zowel de configuratie van Home Assistant (MQTT Discovery) als de actuele status van het energiesysteem. Hierdoor kunnen Home Assistant en andere MQTT-clients automatisch entiteiten ontdekken en de actuele gegevens ontvangen.
De MQTT-module heeft uitsluitend een publicerende functie en beïnvloedt de werking van Project Phoenix niet.

## Ontvangt

Energy State
Decision Context
Plan

## Levert
MQTT Discovery-berichten en 
MQTT statusberichten.

## Wordt aangeroepen door

main.py

## Roept aan

MQTT Broker.

## Afhankelijkheden

MQTT-library.

## Belangrijkste beleidsregels

Publiceert uitsluitend gegevens.
Verzorgt de MQTT Discovery voor Home Assistant.
Publiceert de actuele toestand van Project Phoenix.
Bevat geen energielogica.
Bevat geen plannerlogica.
Stuurt geen apparaten aan.
Wijzigt de Energy State niet.
Een fout in MQTT mag de werking van Project Phoenix niet beïnvloeden.
Andere MQTT-clients kunnen dezelfde topics gebruiken als Home Assistant.

## Code

Nog te ontwikkelen