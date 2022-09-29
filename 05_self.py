from my_exensions.medal import Medal



if __name__ == "__main__":
    th = Medal("thailand", 3, 5, 2)
    print(th.total())
    print(Medal.total(th)) # alternative calling .. th is self

    print(th.dummy(2, 5))
    print(Medal.dummy(th, 2, 5))

    th.rank = 10 
    # rank not include in medal04
    # python can define any class member implicitly (run-time)
    print(th.rank)

    th.ToString()