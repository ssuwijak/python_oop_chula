import re  # regex


class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname.strip().title()
        self.lname = lname.strip().title()

    def __str__(self):
        return "{!r} {!r}".format(self.fname, self.lname)


class Student(Person):
    def __init__(self, s_id, fname, lname) -> None:
        super().__init__(fname, lname)
        self.s_id = self.remove_non_digit(s_id)
        # self.fname = fname
        # self.lname = lname

    def __str__(self):
        return "{:15} {}".format(self.s_id, super().__str__())

    @staticmethod
    def remove_non_digit(s):
        return re.sub(r"[\D]", "", s)  # regex


class ExchangeStudent(Student):
    def __init__(self, s_id, fname, lname, partner_university, ) -> None:
        super().__init__(s_id, fname, lname)
        self.partner_university = partner_university


if __name__ == "__main__":
    s1 = Student("12-34dsf  29304", "john ", "doe")
    print(s1)

    s2 = ExchangeStudent("5678131--323", "jane", "  doe", "MIT")
    print(s2)
