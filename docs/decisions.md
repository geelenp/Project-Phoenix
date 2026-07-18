# Project Phoenix - Architectural Decisions

Dit document bevat de belangrijkste architectuurbeslissingen van Project Phoenix.

Alleen fundamentele keuzes worden hier opgenomen.

---

# ADR-0001

## Titel

Energy State is de Single Source of Truth

## Status

Accepted

## Beslissing

Alle actuele systeeminformatie wordt uitsluitend opgeslagen in de Energy State.

## Gevolgen

- andere componenten bewaren geen eigen kopieën van meetgegevens
- alle componenten lezen uit dezelfde toestand
- inconsistenties worden vermeden

---

# ADR-0002

## Titel

Readers zijn stateless

## Status

Accepted

## Beslissing

Een reader leest één externe databron en retourneert een Python dictionary.

Een reader bewaart zelf geen toestand.

## Gevolgen

- readers zijn eenvoudig te testen
- readers zijn eenvoudig te vervangen
- scheduling gebeurt buiten de reader

---

# ADR-0003

## Titel

YouLess is de primaire netmeter

## Status

Accepted

## Beslissing

Alle netmetingen komen uitsluitend van de YouLess LS120.

## Motivatie

- onafhankelijk van SMA
- hoogste betrouwbaarheid
- P1 is de referentie

## Gevolgen

Alle berekeningen gebruiken uitsluitend deze meting.

---

# ADR-0004

## Titel

Adapter Manager bewaart geen meetgegevens

## Status

Accepted

## Beslissing

De Adapter Manager bepaalt wanneer readers uitgevoerd worden en behandelt fouten.

De Adapter Manager bewaart zelf geen meetgegevens.

Bij een pollingfout blijft de bestaande waarde in de Energy State behouden.

## Gevolgen

- slechts één bron van waarheid
- geen dubbele caches
- planners kunnen de ouderdom van gegevens beoordelen aan de hand van de timestamp in de Energy State
