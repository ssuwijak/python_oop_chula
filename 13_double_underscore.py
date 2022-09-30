# double underscore --> dunder

class Demo1:
    var_public = 111
    _var_protected = 333
    __var_private = 777  # name mangled -> change to _classname__attr  ... _Demo__var_private

    def fn_public(self):
        print("public fn in Demo1")

    def _fn_protected(self):
        print("protected fn in Demo1")

    def __fn_private(self):
        print("private fn in Demo1")


class Demo2(Demo1):
    def __fn_private(self):
        print("private fn in Demo2")

    def __foo__(self):
        pass  # dunder in prefix and sufix can do but it is better to reserve for Python only


class __Demo3:
    # this class cannot be accessed, if it is separated to the new class file
    def fn_public(self):
        print("from __Demo3")


if __name__ == "__main__":
    print(Demo1.__dict__)  # show all attributes of class as dictionary

    print("\ninit. attribute values")
    print(id(Demo1.var_public), Demo1.var_public)
    print(id(Demo1._var_protected), Demo1._var_protected)

    # print(Demo1.__var_private)
    # use the mangled name to access the private attribute
    print(id(Demo1._Demo1__var_private), Demo1._Demo1__var_private)

    print("\ntry to re-assign their values")
    Demo1.var_public = 1
    Demo1._var_protected = 3
    Demo1.__var_private = 7

    print(id(Demo1.var_public), Demo1.var_public)
    print(id(Demo1._var_protected), Demo1._var_protected)
    print(id(Demo1.__var_private), Demo1.__var_private)
    print(id(Demo1._Demo1__var_private), Demo1._Demo1__var_private)
    print("all are immutable (on-the-fly class definition), except the mangled name !!!")

    print(Demo1.__dict__)

    print("\ntry the inheritance")
    a = Demo1()
    a.fn_public()
    a._fn_protected()
    # a.__fn_private()
    a._Demo1__fn_private()

    print("\n")
    b = Demo2()
    print(Demo2.__dict__)
    # b.__fn_private()
    # not override, due to still access the parent function (mangled name)
    b._Demo2__fn_private()
    b._Demo1__fn_private()  # the parent function (mangled name)

    # should be unable to be access, if the class is separated into the new class file.
    c = __Demo3()
    c.fn_public()
