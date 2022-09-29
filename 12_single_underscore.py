import random
import my_exensions.underscore as x # ok to access _private_var
#from my_exensions.underscore import * # fail to access _private_var
#from my_exensions.underscore import _private_var, public_function

def demo1():
    pass

    # in python cli, _ show the last result
    # >>> 3 * 5
    # >>> 15
    # >>> _
    # >>> 15


def demo2():
    # use for unattendly variable name
    for _ in range(5):
        print("hello")

    for i in range(5):
        print(i)

    for _ in range(5):
        print(_)
    
    for _ in range(5):
        print(random.randint(1,6))



def demo3():
    print(x._private_var)
    print(x.public_var)
    
    print(x._private_function(2, 3))
    print(x.public_function(2, 3))




if __name__ == "__main__":
    demo1()
    demo2()
    demo3()
