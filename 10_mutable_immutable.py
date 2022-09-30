def demo_immutable1():
    print("\nimmutable -> same variable name, but different memory address")
    print("immutable of int")
    n = 5
    print("id(n) = {}, n = {}".format(id(n), n))
    n = n + 4
    print("id(n) = {}, n = {}".format(id(n), n))


def demo_immutable2():
    print("\nimmutable -> same variable name, but different memory address")
    print("immutable of string")
    s = "rain"
    print("id(s) = {}, s = {}".format(id(s), s))
    s += "bow"
    print("id(s) = {}, s = {}".format(id(s), s))


def demo_mutable():
    print("\nmutable -> same memory address")
    print("mutable of list (object data type)")

    p = ["rain"]
    print("id(p) = {}, p = {}".format(id(p), p))

    p[0] += "bow"
    print("id(p) = {}, p = {}".format(id(p), p))

    q = p
    print("id(q) = {}, q = {}".format(id(q), q))

    q.append("sunshine")
    print("id(p) = {}, p = {}".format(id(p), p))
    print("id(q) = {}, q = {}".format(id(q), q))


if __name__ == "__main__":
    demo_immutable1()
    demo_immutable2()
    demo_mutable()
