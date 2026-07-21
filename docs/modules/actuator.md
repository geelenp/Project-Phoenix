# Benaming: actuator.py

## Korte beschrijving

Stuurt één specifiek apparaat aan.
Een actuator vertaalt een generieke opdracht van de executor naar de concrete communicatie die nodig is voor het betreffende apparaat.
De actuator bevat uitsluitend apparaatcommunicatie en geen beslissingslogica.

## Ontvangt

Opdracht van executor.py

## Levert

Niets 
Actuator communiceert rechtstreeks met apparaat

## Wordt aangeroepen door

executor.py

## Roept aan

Betreffende apparaat (echarger, tesla API, …)

## Afhankelijkheden

Apparaatspecifieke libraries of API's

## Belangrijkste beleidsregels

Stuurt uitsluitend één apparaat aan.
Bevat geen beslissingslogica.
Bevat geen energielogica.
Bevat geen plannerlogica.
Voert uitsluitend opdrachten uit die door de executor zijn aangeleverd.
Kent uitsluitend de communicatie met het eigen apparaat.
Retourneert geen energiebeslissingen.
Kan onafhankelijk van andere actuators worden ontwikkeld en getest.
Fouten blijven zoveel mogelijk beperkt tot deze actuator.

## Code

Nog te ontwikkelen