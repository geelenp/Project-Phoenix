import time

from pymodbus.client import ModbusTcpClient

from config import HOST, PORT, UNIT


MAX_RETRIES = 10
RETRY_DELAY = 2
TIMEOUT = 3


class SBSClient:

    def __init__(self):

        self.client = None

    def connect(self):

        for attempt in range(1, MAX_RETRIES + 1):

            print(f"Attempt {attempt}/{MAX_RETRIES}")

            client = ModbusTcpClient(
                host=HOST,
                port=PORT,
                timeout=TIMEOUT,
            )

            if client.connect():
                self.client = client
                return True

            client.close()

            time.sleep(RETRY_DELAY)

        return False

    def close(self):

        if self.client is not None:
            self.client.close()

    def read_u32(self, register):

        result = self.client.read_holding_registers(
            address=register,
            count=2,
            device_id=UNIT,
        )

        if result.isError():
            raise RuntimeError(result)

        return (result.registers[0] << 16) | result.registers[1]

    def read_s32(self, register):

        value = self.read_u32(register)

        if value >= 0x80000000:
            value -= 0x100000000

        return value
