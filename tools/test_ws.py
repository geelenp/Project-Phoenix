#!/usr/bin/env python3

import asyncio
import websockets


URI = "ws://192.168.0.217:7070/ws"


async def main():
    print(f"Connecting to {URI}")

    async with websockets.connect(URI) as ws:
        print("Connected\n")

        async for message in ws:
            print(message)


asyncio.run(main())
