from abc import ABC, abstractmethod
# -> Abstract Base Class
from asyncio.proactor_events import _ProactorBaseWritePipeTransport


class Member:
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "id: {}  {} {} (Normal Member)".format(self.id, self.fname, self.lname)

    def Print(self):
        print(self.__str__())


class MemberAbs(Member, ABC):   # multiple inheritance
    @abstractmethod  # required an abstract method/property decorator
    def __str__(self):
        pass    # blank code for abstract and must be defined in the inherit class

    @abstractmethod
    def discount(self):
        pass    # blank code for abstract and must be defined in the inherit class


class Gold(MemberAbs):  # inherit from the abstract class
    def discount(self):
        return .10

    def __str__(self):
        return "id: {}  {} {}  Gold Member Discount: {:.1f}".format(self.id, self.fname, self.lname, self.discount())


class Silver(Member):
    pass


if __name__ == "__main__":
    m = Member("007", "James", "Bond")
    # print(m)
    m.Print()

    # m_abs = MemberAbs()   # cannot use, due to lack of abstractmethod implementation
    # m_abs.Print()

    g = Gold("008", "John", "Doe")
    g.Print()

    s = Silver("009", "Jane", "Doe")
    s.Print()
