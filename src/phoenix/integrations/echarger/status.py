from client import EChargerClient
import registers as reg


def read_status():

    client = EChargerClient()

    if not client.connect():
        return None

    data = {

        "status": client.read(reg.STATUS),
        "status2": client.read(reg.STATUS2),

        "device_class": client.read(reg.DEVICE_CLASS),
        "device_type": client.read(reg.DEVICE_TYPE),
        "firmware": client.read(reg.FIRMWARE),

        "connection_state": client.read(reg.CONNECTION_STATE),
        "connection_state_alt": client.read(reg.CONNECTION_STATE_ALT),

        "r30777": client.read(reg.R30777),
        "r30779": client.read(reg.R30779),
        "r30781": client.read(reg.R30781),

        "r30783": client.read(reg.R30783),
        "r30785": client.read(reg.R30785),
        "r30787": client.read(reg.R30787),

        "r30805": client.read(reg.R30805),
        "r30807": client.read(reg.R30807),
        "r30809": client.read(reg.R30809),
        "r30811": client.read(reg.R30811),
        "r30813": client.read(reg.R30813),
        "r30815": client.read(reg.R30815),
        "r30817": client.read(reg.R30817),
        "r30819": client.read(reg.R30819),
    }

    client.close()

    return data
