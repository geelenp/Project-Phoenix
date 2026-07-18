# Project Phoenix - Architecture

## Doel

Project Phoenix is een lokaal Energy Management System (EMS) dat het energieverbruik van een woning optimaliseert.

Phoenix verzamelt gegevens uit verschillende bronnen, berekent de actuele energietoestand en neemt vervolgens beslissingen om toestellen aan te sturen.

---

## Architectuuroverzicht

```
                PHOENIX
                   │
          Adapter Manager
                   │
              Readers
                   │
            Energy State
                   │
         Decision Context
                   │
              Planner
                   │
              Executor
                   │
             Actuators
```

---

## Componenten

### Phoenix

Phoenix bestuurt de volledige applicatie.

Verantwoordelijkheden:

- starten van het systeem
- uitvoeren van de hoofdloop
- aanroepen van de verschillende componenten

Phoenix bevat geen businesslogica.

---

### Adapter Manager

De Adapter Manager vormt de brug tussen Phoenix en alle externe databronnen.

Verantwoordelijkheden:

- registreren van readers
- bepalen wanneer een reader uitgevoerd wordt
- readers uitvoeren
- fouten afhandelen

De Adapter Manager bewaart zelf geen meetgegevens.

---

### Readers

Elke integratie bevat een reader.

Een reader:

- leest precies één externe databron
- vertaalt de gegevens naar een standaard Python dictionary
- bevat geen businesslogica
- is stateless

Elke integratie bestaat uit:

```
config.py
client.py
reader.py
```

---

### Energy State

De Energy State is de Single Source of Truth van Phoenix.

Alle actuele gegevens bevinden zich hier.

Bij een succesvolle polling worden gegevens bijgewerkt.

Bij een pollingfout blijft de vorige geldige waarde behouden.

Elke dataset bevat een timestamp zodat latere componenten kunnen bepalen hoe oud de informatie is.

---

### Decision Context

De Decision Context vertaalt de ruwe Energy State naar informatie waarop beslissingen genomen kunnen worden.

Voorbeelden:

- overschot PV
- goedkoop laden
- voertuig aangesloten
- batterij bijna vol

---

### Planner

De Planner bepaalt wat Phoenix wil doen.

Hij bevat uitsluitend beslissingslogica.

De Planner stuurt geen hardware rechtstreeks aan.

---

### Executor

De Executor vertaalt een plan naar concrete acties.

Bijvoorbeeld:

- laadstroom wijzigen
- batterij laden
- batterij ontladen

---

### Actuators

Actuators communiceren met de fysieke apparaten.

Ze voeren uitsluitend opdrachten uit.

---

## Ontwerpprincipes

- Energy State is de Single Source of Truth.
- Readers zijn stateless.
- Elke component heeft één duidelijke verantwoordelijkheid.
- Businesslogica bevindt zich uitsluitend in de Planner.
- Hardwarekennis blijft beperkt tot Readers en Actuators.
