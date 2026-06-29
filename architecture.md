# Project Phoenix - Architecture

## Philosophy

Project Phoenix is not built around hardware.

It is built around an energy policy.

Hardware may change over time, but the policy remains the same.

The goal is to maximize self-consumption while respecting a clear set of priorities defined by the user.

---

# Core Principles

## 1. One Source of Truth

Every domain has exactly one primary data source.

| Domain           | Source of Truth |
| ---------------- | --------------- |
| Grid             | YouLess (P1)    |
| Home Battery     | SMA SBS 5.0     |
| Electric Vehicle | Tesla Fleet API |
| EV Charger       | SMA eCharger    |
| Dynamic Prices   | Ecopower        |
| PV Forecast      | Solcast         |

---

## 2. Separation of Responsibilities

The system is divided into four independent layers.

```
Data Providers
        │
        ▼
World Model
        │
        ▼
Policy Engine
        │
        ▼
Execution Layer (EVCC)
```

### Data Providers

Collect information.

They never make decisions.

### World Model

Represents the current state of the house.

Examples:

* Grid importing
* PV surplus
* Battery satisfied
* EV connected
* Fast charging requested

### Policy Engine

Decides what should happen.

It contains the energy strategy.

### Execution Layer

Executes decisions.

Project Phoenix currently uses EVCC for this purpose.

---

# Priority Order

Project Phoenix follows a fixed priority hierarchy.

1. Safety
2. Home battery
3. User intention
4. Self consumption
5. Economic optimisation

Electricity price is only one parameter.

It never overrides higher priorities.

---

# User Intent

Explicit user actions may temporarily modify the strategy.

Examples:

* Fast charging
* Maintenance mode
* Test mode

These actions are intentional overrides.

They are not automatic optimisations.

---

# Reliability

Project Phoenix assumes that communication with the SMA SBS 5.0 may temporarily fail.

The system therefore distinguishes between:

* Valid data
* Stale data
* Invalid data

Energy decisions that depend on battery information are only taken when battery data is considered reliable.

---

# Motto

> Data tells us what **is**.
>
> Policy decides what we **do**.
