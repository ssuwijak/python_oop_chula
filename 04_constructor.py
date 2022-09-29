class Person:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.country = "Thailand"
    
    def __init__(self, fname, lname, country): 
        # unable to have more constructor due to it will use the last one
        self.fname = ""
        self.lname = ""
        self.country = "Thailand"

    def __str__(self):
        return "fname: {}, lname: {}, country: {}".format(self.fname, self.lname, self.country)    
     

class Person2():
    def __init__(self, fname = None, lname = None, country = "Thailand"):
        self.fname = fname
        self.lname = lname
        self.country = country

    def __str__(self):
        return "fname: {}, lname: {}, country: {}".format(self.fname, self.lname, self.country)    
             

if __name__ == "__main__":
    #p1 = Person()
    #print(p1.fname)
    #print(p1.country)

    p2 = Person("aaa", "bbb", "ccc")
    print(p2)

    p3 = Person2("AAA", "BBB")
    print(p3)
