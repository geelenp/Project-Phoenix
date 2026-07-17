"""
Project Phoenix
SMA eCharger Modbus Register Map

Only registers used by Phoenix P1 are defined here.
"""

#
# Device Information
#

DEVICE_CLASS = 30051
DEVICE_TYPE = 30053
FIRMWARE = 30055

#
# General Status
#

STATUS = 30201
MAX_POWER = 30233

#
# Active Power (W)
#

POWER_L1 = 30777
POWER_L2 = 30779
POWER_L3 = 30781

#
# Grid Voltage (FIX2 -> divide by 100)
#

VOLTAGE_L1 = 30783
VOLTAGE_L2 = 30785
VOLTAGE_L3 = 30787

#
# Reactive Power (VAr)
#

REACTIVE_TOTAL = 30805
REACTIVE_L1 = 30807
REACTIVE_L2 = 30809
REACTIVE_L3 = 30811

#
# Apparent Power (VA)
#

APPARENT_TOTAL = 30813
APPARENT_L1 = 30815
APPARENT_L2 = 30817
APPARENT_L3 = 30819

#
# Communication
#

SPEEDWIRE_STATUS = 30929

#
# Total Active Power (W)
#
# Strongly confirmed by measurements.
# Equals the total charging power.
#

TOTAL_ACTIVE_POWER = 35457
