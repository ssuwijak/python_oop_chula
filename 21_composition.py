# composition -> implement classes in a class (not inherit)

from datetime import date


class PersonData:
    def __init__(self, title, fname, lname) -> None:
        self.title = title
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "{} {} {}".format(self.title, self.fname, self.lname)


class Person:
    def __init__(self, dataEn: PersonData, dataTh: PersonData, bd: date) -> None:
        self.dataEn = dataEn
        self.dataTh = dataTh
        self.bd = bd

    def __str__(self):
        return "{}\n{}\n{}".format(self.dataEn, self.dataTh, self.bd)


if __name__ == "__main__":
    d1 = PersonData("Mr.", "John", "Doe")
    print(d1)

    d2 = PersonData("นาย", "จอห์น", "โด")
    print(d2)

    print("*" * 40)

    p1 = Person(d1, d2, date(1994, 4, 22))
    print(p1)

    print("*" * 40)

    p2 = Person(PersonData("Ms.", "Jane", "Doe"),
                PersonData("น.ส.", "เจน", "โด"),
                date(1995, 4, 1))
    print(p2)
