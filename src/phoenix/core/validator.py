class PhoenixValidator:
    """
    Validates the current PhoenixState.

    The validator never changes state.
    It only reports problems.
    """

    def validate(self, state):
        warnings = []

        #
        # Grid
        #

        if state.grid_power is None:
            warnings.append("Grid power unavailable")

        #
        # Home
        #

        if state.home_power is None:
            warnings.append("Home power unavailable")

        #
        # PV
        #

        if state.pv_power is None:
            warnings.append("PV power unavailable")
        elif state.pv_power < 0:
            warnings.append("PV power negative")

        #
        # Battery
        #

        if state.battery_soc is None:
            warnings.append("Battery SOC unavailable")
        elif not 0 <= state.battery_soc <= 100:
            warnings.append(f"Battery SOC invalid ({state.battery_soc})")

        if (
            state.battery_capacity is not None
            and state.battery_capacity <= 0
        ):
            warnings.append("Battery capacity invalid")

        return warnings
