class FileMan:
    def __init__(self, debugMode=False):
        self._debugMode = debugMode
        self._enabled = True

    def _log(self, msg: str):
        if self._debugMode:
            print(msg)

    @staticmethod
    def IsEmptyStr(value: str):
        value = value.strip()
        return value == '' or len(value) < 1, value
