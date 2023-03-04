import os


class Directory:
    @staticmethod
    def log(msg: str, silentMode=True):
        if not silentMode:
            print(msg)

    @staticmethod
    def IsEmptyStr(value: str):
        value = value.strip()
        return value == '' or len(value) < 1, value

    @staticmethod
    def GetName(fullName: str):
        ret, value = Directory.IsEmptyStr(fullName)
        return os.path.basename(value)

    @staticmethod
    def GetPath(fullName: str):
        ret, value = Directory.IsEmptyStr(fullName)
        return os.path.dirname(value)

    @staticmethod
    def Exists(name: str, isFullName=True):
        ret, value = Directory.IsEmptyStr(name)
        ret = False if ret else True  # ret = ret ? False : True

        if ret:
            ret = False

            if not isFullName:
                value = os.path.join(os.getcwd(), value)

            if os.path.exists(value):
                ret = os.path.isdir(value)

        return ret

    @staticmethod
    def Create(name: str, isFullName=True):
        ret, value = Directory.IsEmptyStr(name)
        ret = False if ret else True  # ret = ret ? False : True

        if ret:
            if not isFullName:
                value = os.path.join(os.getcwd(), value)

            if not Directory.Exists(value):
                try:
                    os.makedirs(value)
                except Exception as ex:
                    ret = False

        return ret

    @staticmethod
    def Rename(currentName: str, newName: str, isFullName=True):
        src = ["", True, True]  # name, isempty, exists
        dest = ["", True, True]
        cur_path = os.getcwd()
        work_path = ""

        src[1], src[0] = Directory.IsEmptyStr(currentName)
        dest[1], dest[0] = Directory.IsEmptyStr(newName)

        ret = False if src[1] or dest[1] else True

        if ret:
            if isFullName:
                work_path = Directory.GetPath(currentName)
            else:
                work_path = cur_path

            src[0] = Directory.GetName(currentName)
            dest[0] = Directory.GetName(newName)

            src[2] = Directory.Exists(os.path.join(work_path, src[0]))
            dest[2] = Directory.Exists(os.path.join(work_path, dest[0]))

            ret = src[2] and not dest[2]

        if ret:
            os.chdir(work_path)
            try:
                os.rename(src[0], dest[0])
            except Exception as ex:
                ret = False

            os.chdir(cur_path)

        return ret

    @staticmethod
    def Delete(name, delSubDirs=False, isFullName=True):
        ret, value = Directory.IsEmptyStr(name)
        ret = False if ret else True  # ret = ret ? False : True

        if ret:
            if not isFullName:
                value = os.path.join(os.getcwd(), value)

            ret = Directory.Exists(value)

        if ret:
            counters = [0, 0]  # files, dirs

            if delSubDirs:
                for root, dirs, files in os.walk(value, topdown=False):
                    for name in files:
                        fullName = os.path.join(root, name)
                        try:
                            os.remove(fullName)
                            counters[0] += 1
                            print(
                                f" {counters[0]}) file delete ok, '{fullName}'")
                        except Exception as ex:
                            print(f" file delete failed, '{fullName}', {ex}")
                            ret = False
                            break

                    for name in dirs:
                        fullName = os.path.join(root, name)
                        try:
                            os.rmdir(fullName)
                            counters[1] += 1
                            print(
                                f"{counters[1]}) DIR delete ok, '{fullName}'")
                        except Exception as ex:
                            print(f"DIR delete failed, '{fullName}', {ex}")
                            ret = False
                            break

            '''
            for idx, di in enumerate(Directory.GetDiectories(value)):
                if delSubFolders:
                    Directory.Delete(os.path.join(value, di), delSubFolders)

            for idx, f in enumerate(Directory.GetFiles(value)):
                if delSubFolders:
                    print(f"{idx+1}) '{os.path.join(value, f)}' is deleting")
                    os.remove(os.path.join(value, f))
            '''

            if ret and Directory.Exists(value):
                try:
                    os.rmdir(value)
                    ret = True
                except Exception as ex:
                    print(f"DIR delete failed, '{value}', {ex}")
                    ret = False

                '''
                obj_count = len(Directory.GetDirectories(value)) + \
                    len(Directory.GetFiles(value))

                if obj_count == 0:
                    os.rmdir(value)
                    ret = True
                    print(f"'{value}' was deleted")
                else:
                    print(f"\tobj count of '{value}'= {obj_count}")
                    ret = False
                '''

        return ret

    @staticmethod
    def GetDirectories(fullPath: str):
        isEmpty, value = Directory.IsEmptyStr(fullPath)

        if isEmpty:
            return []
        elif Directory.Exists(value):
            return [name for name in os.listdir(value) if os.path.isdir(os.path.join(value, name))]
        else:
            return []

    @staticmethod
    def GetFiles(fullPath: str):
        isEmpty, value = Directory.IsEmptyStr(fullPath)

        if isEmpty:
            return []
        elif Directory.Exists(value):
            return [name for name in os.listdir(value) if os.path.isfile(os.path.join(value, name))]
        else:
            return []


if __name__ == '__main__':
    p = r"d:\xxx"
    print('p=' + p)
    # ret = Directory.Delete(p, False)
    # ret = ''

    ret = Directory.Create(p)
    print(Directory.Exists(p))

    print(Directory.GetName(p))
    print(Directory.GetPath(p))

    ret = Directory.Rename(p, r"xxx2")

    p = r"d:\xxx2"
    print(Directory.Exists(p))

    #ret = Directory.Delete(p)
    print(Directory.Exists(p))
