# Project Phoenix - Architectural Decisions

# ADR-0001

## Titel

Primary Grid Meter

## Status

Accepted

## Beslissing

Alle netmetingen komen uitsluitend van de YouLess LS120.

## Motivatie

- onafhankelijk van SMA
- hoogste betrouwbaarheid
- P1 is de referentie
- één enkele source of truth

## Gevolgen

Alle laadbeslissingen gebruiken uitsluitend deze meting.

# ADR-0002 – Last Known Good Values

## Beslissing

Voor databronnen waarvan tijdelijke communicatie-uitval verwacht wordt (zoals de SMA SBS) gebruikt Project Phoenix een Last Known Good-mechanisme met een maximale geldigheidsduur per datatype.

