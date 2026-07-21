# Project Phoenix - Energy Planner

## Planner philosophy

The planner determines how available energy is distributed.

It does **not** communicate with devices.

The planner only produces an execution plan.

## Priority order

When surplus energy is available, the planner uses the following priority:

1. SBS (home battery)
2. EV charger
3. Boiler
4. Export to the grid

When energy is scarce, the reverse applies:

1. Reduce export
2. Boiler
3. EV charger
4. SBS discharge (within configured limits)

## Responsibilities

### Readers

Read measurements from devices.

### Energy State

Single Source of Truth.

### calculate()

Derive power flows and status.

### Decision Context

Determine the current situation.

### Planner

Decide **what** should happen.

### Executor

Decide **how** to perform the requested actions.
