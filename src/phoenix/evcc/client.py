import asyncio
import json
from collections.abc import Awaitable, Callable

import websockets


class EvccClient:
    """Connects to the evcc websocket and forwards every event."""

    def __init__(self, url: str, callback: Callable[[dict], Awaitable[None]]):
        self.url = url
        self.callback = callback

    async def run(self):
        while True:
            try:
                async with websockets.connect(self.url) as ws:
                    print(f"Connected to {self.url}")

                    async for message in ws:
                        event = json.loads(message)
                        await self.callback(event)

            except Exception as err:
                print(f"EVCC disconnected: {err}")
                print("Reconnecting in 5 seconds...")
                await asyncio.sleep(5)
