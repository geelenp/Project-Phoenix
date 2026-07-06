from copy import deepcopy

from phoenix.core.derived import DerivedState


class PhoenixState:
    """
    Holds the current evcc state.

    The first websocket message is a complete snapshot.
    Every following websocket message is a delta update.

    Phoenix always works on the merged state.
    """

    def __init__(self):
        self.data = {}
        self.derived = DerivedState(self)

    def update(self, event: dict):
        self._merge(self.data, event)

    def snapshot(self):
        return deepcopy(self.data)

    #
    # Grid
    #

    @property
    def grid_power(self):
        return self.data.get("grid", {}).get("power")

    @property
    def grid_energy(self):
        return self.data.get("grid", {}).get("energy")

    #
    # Home
    #

    @property
    def home_power(self):
        return self.data.get("homePower")

    #
    # PV
    #

    @property
    def pv_power(self):
        return self.data.get("pvPower")

    #
    # Battery
    #

    @property
    def battery_power(self):
        return self.data.get("battery", {}).get("power")

    @property
    def battery_soc(self):
        return self.data.get("battery", {}).get("soc")

    @property
    def battery_capacity(self):
        return self.data.get("battery", {}).get("capacity")

    #
    # Diagnostics
    #

    @property
    def api_ready(self):
        return self.data.get("apiReady")

    @property
    def evcc_version(self):
        return self.data.get("version")

    @property
    def site_title(self):
        return self.data.get("siteTitle")

    #
    # Internal
    #

    def _merge(self, target, source):
        for key, value in source.items():
            if (
                key in target
                and isinstance(target[key], dict)
                and isinstance(value, dict)
            ):
                self._merge(target[key], value)
            else:
                target[key] = value
