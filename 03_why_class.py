def demo_tuple():
    p = "joe", "gomez", 12  # tuple
    print("tuple")
    print(p)
    print(p[1])  # tuple access by index


def demo_dict():
    p = {"fname": "joe", "lname": "gomez", "number": 12}
    print("dict")
    print(p)
    print(p["lname"])  # dict access by key


class Player:
    pass


class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number


def demo_class():
    p = Player()
    p.fname = "joe"  # on the fly attributes
    p.lname = "gomez"
    p.number = 12
    print("class")
    print(p)
    print(p.lname)  # no intellisent


def demo_class2():
    p = Player2("joe", "gomez", 12)
    print("class2")
    print(p)
    print(p.lname)  # intellisent work after type dot


if __name__ == '__main__':
    demo_tuple()
    demo_dict()
    demo_class()
    demo_class2()
