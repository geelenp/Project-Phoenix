from pymodbus.client import ModbusTcpClient

from config import HOST, PORT, UNIT


class EChargerClient:

    def __init__(self):

        self.client = ModbusTcpClient(
            host=HOST,
            port=PORT,
            timeout=2,
        )

    def connect(self):

        return self.client.connect()

    def close(self):

        self.client.close()

    def read(self, register):

        result = self.client.read_holding_registers(
            address=register,
            count=2,
            device_id=UNIT,
        )

        if result.isError():
            return None

        r1, r2 = result.registers

        # SMA NaN values
        if r1 == 0xFFFF and r2 == 0xFFFF:
            return None

        if r1 == 0x8000 and r2 == 0:
            return None

        return (r1 << 16) | r2
