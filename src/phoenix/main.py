import asyncio

from phoenix.core.engine import PhoenixEngine
from phoenix.evcc.client import EvccClient


engine = PhoenixEngine()


async def handle_event(event: dict):
    engine.process(event)


async def main():
    client = EvccClient(
        "ws://192.168.0.217:7070/ws",
        handle_event,
    )

    await client.run()


if __name__ == "__main__":
    asyncio.run(main())
