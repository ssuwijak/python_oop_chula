class PersonJavaStyle:
    def __init__(self, fname, lname, blood) -> None:
        self.fname = fname
        self.lname = lname
        # self.blood = blood
        self.setBlood(blood)

    def getBlood(self):
        return self._blood

    def setBlood(self, value):
        value = value.upper().strip()

        if value in ["A", "B", "AB", "O"]:
            self._blood = value
        else:
            raise ValueError("invalid blood group")

    def __str__(self):
        return "{} {}, blood group: {}".format(self.fname, self.lname, self._blood)


class PersonPythonStyle:
    def __init__(self, fname, lname, blood) -> None:
        self.fname = fname
        self.lname = lname
        self.Blood = blood

    @property
    def Blood(self):  # getter
        return self._blood

    @Blood.setter
    def Blood(self, value):  # setter
        value = value.upper().strip()

        if value in ["A", "B", "AB", "O"]:
            self._blood = value
        else:
            raise ValueError("invalid blood group")

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        self._fname = value.strip().title()

    def __str__(self):
        return "{} {}, blood group: {}".format(self.fname, self.lname, self._blood)


if __name__ == "__main__":
    p1 = PersonJavaStyle("Peter", "Parker1", "A")
    p1.setBlood("O")
    print(p1)

    p2 = PersonPythonStyle("xpeter", "Parker2", "A")
    p2.Blood = "b"
    print(p2)
