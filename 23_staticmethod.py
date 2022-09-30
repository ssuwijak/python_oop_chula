class Person:
    def __init__(self, name) -> None:
        self.name = name

    def introduce(self):
        print("my name is " + self.name)

    @staticmethod
    def hi(n):
        print("Hi, " * n)


if __name__ == "__main__":
    p = Person("Bob")
    p.introduce()
    Person.hi(10)