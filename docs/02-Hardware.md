# Hardware Configuration

This document is the single source of truth for the physical Project Phoenix installation.

---

# Grid

| Property  | Value         |
|-----------|---------------|
| Component | Youless LS120 |
| Role      | Grid meter    |
| Protocol  | HTTP          |
| IP        | 192.168.0.218 |

---

# Battery

| Property  | Value                     |
|-----------|---------------------------|
| Component | SMA Sunny Boy Storage 5.0 |
| Role      | Battery inverter          |
| Protocol  | Modbus TCP                |
| IP        | 192.168.0.201             |
| Port      | 502                       |
| Unit ID   | 3                         |
| Capacity  | 16 kWh                    |

---

# PV

| Property  | Value                                                          |
|-----------|----------------------------------------------------------------|
| Component | Eastron SDM120M                                                |
| Role      | Total PV production meter                                      |
| Protocol  | Modbus RTU                                                     |
| Device    | /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_BG01X9OK-if00-port0 |
| Slave ID  | 1                                                              |
| Baudrate  | 9600                                                           |
| Serial    | 8N1                                                            |

## PV Inverters

- SMA Sunny Boy 3300TL
- SMA Sunny Boy 1700TL

The SDM120M measures the combined AC production of both PV inverters.

---

# EV Charger

| Property  | Value             |
|-----------|-------------------|
| Component | SMA EV Charger    |
| Role      | EV charger        |
| Protocol  | Modbus TCP        |
| IP        | 192.168.0.135     |

---

# Home Manager

| Property  | Value              |
|-----------|--------------------|
| Component | SMA Home Manager 2 |
| IP        | 192.168.0.225      |

Project Phoenix does not communicate with the Home Manager.

---

# Phoenix Data Sources

| Phoenix Value | Source                    |
|---------------|---------------------------|
| `grid.*`      | Youless LS120             |
| `battery.*`   | SMA Sunny Boy Storage 5.0 |
| `pv.*`        | Eastron SDM120M           |
| `ev.*`        | SMA EV Charger            |
| `forecast.*`  | Solcast                   |
| `price.*`     | ENTSO-E                   |

---

# Notes

Project Phoenix communicates only with the devices listed in this document.

Home Assistant, the MQTT broker and other software components are part of the software architecture and are documented separately.