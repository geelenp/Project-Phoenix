import asyncio

from phoenix.core.state import PhoenixState
from phoenix.core.validator import PhoenixValidator
from phoenix.evcc.client import EvccClient


state = PhoenixState()
validator = PhoenixValidator()


async def handle_event(event: dict):
    state.update(event)

    print(
        f"Grid={state.grid_power:>6} W | "
        f"PV={state.pv_power:>6.0f} W | "
        f"Home={state.home_power:>6.0f} W | "
        f"Battery={state.battery_soc:>3}% | "
        f"EV={'Connected' if state.car_connected else 'Disconnected'} | "
        f"{'Charging' if state.car_charging else 'Idle'}"
    )

    warnings = validator.validate(state)

    if warnings:
        print("\nValidator")
        for warning in warnings:
            print(f"  WARNING: {warning}")


async def main():
    client = EvccClient(
        "ws://192.168.0.217:7070/ws",
        handle_event,
    )

    await client.run()


if __name__ == "__main__":
    asyncio.run(main())
