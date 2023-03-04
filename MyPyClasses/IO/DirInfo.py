import os
from FileMan import FileMan
from Directory import Directory


class DirInfo(FileMan):
    def __init__(self, fullName: str):
        super().__init__()

        self._fullName = ''
        self._name = ''
        self._path = ''

        isEmpty, value = DirInfo.IsEmptyStr(fullName)

        if not isEmpty:
            self._fullName = value
            if self.Exists():
                self._name = os.path.basename(self._fullName)
                self._path = os.path.dirname(self._fullName)

    def __str__(self):
        return self._fullName

    @property
    def FullName(self):
        return self._fullName

    @property
    def Name(self):
        return self._name

    @property
    def Path(self):
        return self._path

    def Exists(self):
        ret, _ = DirInfo.IsEmptyStr(self._fullName)
        ret = False if ret else True

        if ret:
            ret = False

            if os.path.exists(self._fullName):
                ret = os.path.isdir(self._fullName)

        return ret

    def Create(self):
        ret, _ = DirInfo.IsEmptyStr(self._fullName)
        ret = False if ret else True

        if ret:
            if not self.Exists():
                try:
                    os.makedirs(self._fullName)
                except Exception as ex:
                    ret = False
        return ret

    def CreateSubDir(self, dirName: str):
        ret, value = DirInfo.IsEmptyStr(dirName)
        ret = False if ret else True

        if ret:
            value = os.path.join(self._fullName, value)
            if not Directory.Exists(value):
                ret = Directory.Create(value)

        return ret

    def Rename(self, newName: str):
        dest = ["", False, False]  # name, isempty, exists
        ret = newName[0].isalpha
        dest[1], dest[0] = Directory.IsEmptyStr(newName)
        dest[0] = Directory.GetName(newName)

        return True

    def Copy(self, newPath: str):
        return True

    def Delete(self, delSubDirs=False):
        return True

    def GetDirectories(self):
        if self.Exists():
            value = self._fullName
            return [name for name in os.listdir(value) if os.path.isdir(os.path.join(value, name))]
        else:
            return []

    def GetFiles(self):
        if self.Exists():
            value = self._fullName
            return [name for name in os.listdir(value) if os.path.isfile(os.path.join(value, name))]
        else:
            return []


if __name__ == '__main__':
    # print(FileMan.)
    d = DirInfo("d:\Beng  ")
    print(f"'{d}' exists = {d.Exists()}")
