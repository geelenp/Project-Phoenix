# Project Phoenix Architecture

## Purpose

Project Phoenix is a local Energy Management System (EMS) that optimizes residential energy flows.

The system collects measurements from multiple sources, maintains a central Energy State, determines the current energy situation and generates an execution plan for connected devices.

---

# Architecture Overview

```
                         Home Assistant
                              │
                     MQTT Discovery / REST
                              │
         ┌────────────────────┴────────────────────┐
         │                                         │
     MQTT Publisher                        REST API
         │                                         │
         └────────────────────┬────────────────────┘
                              │
                        Decision Output
                              ▲
                              │
Readers → Energy State → calculate() → Decision Context
                                      │
                                      ▼
                                  Targets
                                      │
                                      ▼
                                 Constraints
                                      │
                                      ▼
                                   Planner
                                      │
                                      ▼
                                     Plan
                                      │
                                      ▼
                                   Executor
                                      │
                                      ▼
                                  Actuators
```

---

# Architecture

## Phoenix

Phoenix starts the application, initializes all modules and executes the main loop.

Phoenix itself contains no business logic.

---

## Manager

The Manager controls all Readers.

Responsibilities:

- initialize readers
- execute readers according to their polling interval
- update the Energy State
- isolate reader failures

The Manager contains no energy logic.

---

## Readers

Readers retrieve data from external systems.

Each Reader:

- communicates with one external system
- converts data into the internal format
- updates the Energy State
- contains no business logic

Readers are independent and stateless.

---

## Energy State

The Energy State is the single source of truth of Project Phoenix.

It contains the latest known values received from all Readers.

If a Reader fails, previously received values remain available until updated.

---

## calculate()

The calculate() module derives additional values from the Energy State.

Examples include:

- household consumption
- battery power
- available PV surplus
- energy balance

The calculated values are added to the Energy State.

---

## Decision Context

The Decision Context converts measurements into information that can be used for decision making.

Examples include:

- surplus available
- battery nearly full
- vehicle connected
- cheap electricity
- forecast shortage

---

## Targets

Targets describe the desired system behaviour.

Examples include:

- maximize self-consumption
- minimize energy costs
- maintain battery reserve

Targets define *what* the system wants to achieve.

---

## Constraints

Constraints define operational limits.

Examples include:

- battery limits
- charger limits
- hardware capabilities
- user settings

Constraints define *what is allowed*.

---

## Planner

The Planner combines:

- Decision Context
- Targets
- Constraints

The result is a hardware-independent execution Plan.

---

## Plan

The Plan contains the intended actions.

Examples:

- charge EV at 8 A
- charge battery
- stop export

The Plan contains no hardware-specific implementation.

---

## Executor

The Executor translates the Plan into device-specific commands.

---

## Actuators

Actuators communicate with physical hardware.
They execute commands and contain no decision logic.

---

## Output Layer

Several modules publish information for external consumers.

These include:

- Energy State
- Decision Context
- Plan

The information can be published through:

- MQTT
- REST
- Logger

These modules never influence decision making.

---

## Home Assistant

Home Assistant is the user interface of Project Phoenix.
It visualizes data, allows user interaction and can issue commands.
Energy management decisions remain entirely within Project Phoenix.

---

# Design Principles

- Energy State is the single source of truth.
- Readers and Actuators isolate hardware-specific code.
- Every module has a single responsibility.
- Decision making is separated from hardware control.
- The Planner produces hardware-independent Plans.
- The Executor performs hardware-specific execution.
- Home Assistant is a presentation layer only.
- VS Code is the source of truth for the project.