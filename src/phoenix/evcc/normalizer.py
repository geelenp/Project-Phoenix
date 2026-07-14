class EventNormalizer:
    """
    Converts evcc websocket delta events into nested dictionaries.

    Example:

        {"loadpoints.0.connected": True}

    becomes

        {
            "loadpoints": [
                {
                    "connected": True
                }
            ]
        }
    """

    @classmethod
    def normalize(cls, event: dict) -> dict:
        result = {}

        for key, value in event.items():
            cls._insert(result, key.split("."), value)

        return result

    @classmethod
    def _insert(cls, obj, path, value):
        part = path[0]

        #
        # last element
        #

        if len(path) == 1:
            obj[part] = value
            return

        #
        # list index
        #

        if path[1].isdigit():

            obj.setdefault(part, [])

            index = int(path[1])

            while len(obj[part]) <= index:
                obj[part].append({})

            cls._insert(obj[part][index], path[2:], value)
            return

        #
        # dictionary
        #

        obj.setdefault(part, {})

        cls._insert(obj[part], path[1:], value)
