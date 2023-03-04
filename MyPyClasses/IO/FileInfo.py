import os

from enum import Enum


class OS(Enum):
    Windows = 0
    LinuxUnix = 1
    Mac = 2


class FileInfo:
    def __init__(self, fullName):
        value = fullName.strip()
        if len(value) > 0:
            self._fullName = value
            self._exists = self.Exists()

            if self._exists:
                self._fileName = os.path.basename(self._fullName)
                self._fileNameNoExt = self._fileName.split('.')[0]
                self._extension = self._fileName.split('.')[1]
                self._createdDate = ""
                self._modifiedDate = ""
                self._size = 1
            else:
                self._fileName = ""
                self._fileNameNoExt = ""
                self._extension = ""
                self._createdDate = ""
                self._modifiedDate = ""
                self._size = 0

    def Exists(self, fullName=""):
        ret = False

        if self._fileExists:
            ret = os.path.exists(
                self._fullName) and os.path.isfile(self._fullName)
            self._fileExists = ret
        elif value == "" or len(value) == 0:
            pass
        else:
            value = fullName.strip()
            ret = os.path.exists(value) and os.path.isfile(value)

        return ret
