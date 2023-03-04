class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def ToString1(self):
        return "ToString1 ... fname: {}, lname: {}, age: {}".format(self.fname, self.lname, self.age)

    def ToString2(self):
        print("ToString2 ...")
        a = vars(self)
        print(a)  # return a dictionary  key=attribute value=its value
        return ""

    def ToString3(self):
        a = vars(self)
        s = ["ToString3 ... {:8}: {}".format(k, v) for k, v in a.items()]
        return "\n".join(s)

    def ToString4(self):
        # specify attribute manually to fix the attribute order
        attrs = ("fname", "lname", "age")
        s = ["ToString4 ... {:8}: {}".format(
            a, getattr(self, a)) for a in attrs]
        return "\n".join(s)


if __name__ == "__main__":
    p = Person("Peter", "Parker", 26)
    print(p.ToString1())
    print(p.ToString2())
    print(p.ToString3())
    print(p.ToString4())
