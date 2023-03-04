# mutable = changable
# immutable = read only
# https://realpython.com/python-pass-by-reference/
# https://www.guru99.com/mutable-and-immutable-in-python.html
# function arguments .. by ref vs by val

'''
Python Immutable Data Types:

Class	Explanation	Immutable or not
------------------------------------
Bool	Boolean value	Immutable
Int	Integer value (magnitude can be arbitrary)	Immutable
Float	Floating point number	Immutable
List	Sequence of objects of mutable nature	Mutable
Tuple	Sequence of objects of immutable nature	Immutable
Str	Character /string	Immutable
Set	set of distinct objects that are of Unordered nature	Mutable
Frozenset	Set class of immutable nature	Immutable
Dict	Dictionary or associative mapping	Mutable

'''

def demo_immutable1():
    print("\nimmutable -> same variable name, but different memory address")
    print("immutable of int")
    n = 5
    print("id(n) = {}, n = {}".format(id(n), n))
    n = n + 4
    print("id(n) = {}, n = {}".format(id(n), n))
    print("** same var name but different address")


def demo_immutable2():
    print("\nimmutable -> same variable name, but different memory address")
    print("immutable of string")
    s = "rain"
    print("id(s) = {}, s = {}".format(id(s), s))
    s += "bow"
    print("id(s) = {}, s = {}".format(id(s), s))
    print("** same var name but different address")


def demo_mutable():
    print("\nmutable -> same memory address")
    print("mutable of list (object data type)")

    p = ["rain"]
    print("id(p) = {}, p = {}".format(id(p), p))

    p[0] += "bow"
    print("id(p) = {}, p = {}".format(id(p), p))

    q = p # set to the same reference address
    print("id(q) = {}, q = {}".format(id(q), q))

    q.append("sunshine")
    print("id(p) = {}, p = {}".format(id(p), p))
    print("id(q) = {}, q = {}".format(id(q), q))
    print("** diff var name but same address")


if __name__ == "__main__":
    demo_immutable1()
    demo_immutable2()
    demo_mutable()
