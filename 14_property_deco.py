class Student:
    def __init__(self, s_id, fname, lname) -> None:
        self.s_id = s_id
        self.fname = fname
        self.lname = lname
        # self.full_name = "{} {}".format(self.fname, self.lname)

    def full_name(self):    # function or method
        return "{} {}".format(self.fname, self.lname)
    
    @property # apply property decorator and the next like a method
    def full_name2(self):   # property
        return "{} {}".format(self.fname, self.lname)

    @property
    def short_name(self):
        return "{}.{}".format(self.fname, self.lname[:1])

if __name__ == "__main__":
    a = Student("361016003", "John", "Mayer")
    print(a.full_name())
    print(a.full_name2)
    print(a.short_name)

