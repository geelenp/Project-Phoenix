from copy import deepcopy


class PhoenixState:
    """
    Holds the current evcc state.

    The first websocket message is a complete snapshot.
    Every following websocket message is a delta update.

    Phoenix always works on the merged state.
    """

    def __init__(self):
        self.data = {}

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

    @property
    def importing(self):
        return (self.grid_power or 0) > 0

    @property
    def exporting(self):
        return (self.grid_power or 0) < 0

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

    @property
    def pv_energy(self):
        return self.data.get("pvEnergy")

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

    @property
    def battery_energy(self):
        return self.data.get("battery", {}).get("energy")

    #
    # EV
    #

    @property
    def car_connected(self):
        loadpoints = self.data.get("loadpoints", [])
        if not loadpoints:
            return False
        return loadpoints[0].get("connected", False)

    @property
    def car_charging(self):
        loadpoints = self.data.get("loadpoints", [])
        if not loadpoints:
            return False
        return loadpoints[0].get("charging", False)

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
