from my_exensions.medal import Medal

if __name__ == "__main__":
    th = Medal("thailand", 3, 5, 12)
    print(th)
    th.ToString()

    # create a new list
    m = [
        Medal("indonesia", 3, 6, 14),
        Medal("malaysia", 2, 3, 10),
        Medal("myanmar", 1, 7, 15)
    ]

    for c in m:
        print(c)
        c.ToString()
