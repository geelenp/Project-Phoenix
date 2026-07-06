class DerivedState:
    """
    Derived values calculated from PhoenixState.

    This class never stores state.
    It only derives facts from the current PhoenixState.
    """

    def __init__(self, state):
        self.state = state

    #
    # Grid
    #

    @property
    def importing(self):
        power = self.state.grid_power
        return power is not None and power > 0

    @property
    def exporting(self):
        power = self.state.grid_power
        return power is not None and power < 0

    #
    # Battery
    #

    @property
    def available_charge(self):
        if (
            self.state.battery_soc is None
            or self.state.battery_capacity is None
        ):
            return None

        return (
            self.state.battery_capacity
            * (100 - self.state.battery_soc)
            / 100
        )

    @property
    def available_discharge(self):
        if (
            self.state.battery_soc is None
            or self.state.battery_capacity is None
        ):
            return None

        return (
            self.state.battery_capacity
            * self.state.battery_soc
            / 100
        )
