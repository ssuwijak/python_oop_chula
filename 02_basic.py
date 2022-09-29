class Player:
    def __init__(self): # dunder -> double underscore
        self.fname = ""
        self.lname = ""
        self.number = ""

class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

if __name__ == '__main__':
    p1 = Player()
    p1.fname = ""
    p1.lname = ""
    p1.number = 1

    p2 = Player2("ccc", "ccc", 2)
    p3 = Player2("bbb", "bbb", 23)

    p4_tuple = ("ddd", "ddd", 33)   # tuple
    print(p4_tuple[0])

