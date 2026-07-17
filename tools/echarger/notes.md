# SMA eCharger Notes

## Confirmed registers

| Register | Description | Status |
|----------|-------------|--------|
|30051|Device class|Confirmed|
|30053|Device type|Confirmed|
|30055|Firmware version|Confirmed|
|30201|Status (307 = OK)|Confirmed|
|30233|Maximum charging power (11000 W)|Confirmed|
|30777|Active power L1|Confirmed|
|30779|Active power L2|Confirmed|
|30781|Active power L3|Confirmed|
|30783|Voltage L1 (÷100)|Confirmed|
|30785|Voltage L2 (÷100)|Confirmed|
|30787|Voltage L3 (÷100)|Confirmed|
|30805|Reactive power total|Confirmed|
|30807|Reactive power L1|Confirmed|
|30809|Reactive power L2|Confirmed|
|30811|Reactive power L3|Confirmed|
|30813|Apparent power total|Confirmed|
|30815|Apparent power L1|Confirmed|
|30817|Apparent power L2|Confirmed|
|30819|Apparent power L3|Confirmed|
|30929|Speedwire status|Confirmed|
|35457|Total active charging power|Confirmed by measurements|

---

## Measurements

### Charging stopped

- Status = 307
- Total active power = 0 W

### EV disconnected

- Status = 307
- Total active power = 0 W

### Charging (~6.8 kW)

L1 = 1376 W

L2 = 1372 W

L3 = 1388 W

Total register = 6778 W

### Charging (~8.2 kW)

L1 = 2702 W

L2 = 2737 W

L3 = 2760 W

Sum = 8199 W

Register 35457 = 8199 W

### Charging (~10.9 kW)

L1 = 3616 W

L2 = 3559 W

L3 = 3659 W

Total register = 10942 W

---

## Design decisions

- Phoenix uses register 35457 as the preferred total charging power.
- The sum of L1, L2 and L3 is kept as a fallback during development.
- Voltages are FIX2 values and divided by 100.
- Only registers used by Phoenix are defined in `registers.py`.

---

## Open questions

- Meaning of status value 307.
- Meaning of device class 8008.
- Meaning of device type 19143.
- Exact interpretation of Speedwire status.