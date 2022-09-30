class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):
        return self.gold + self.silver + self.bronze

    def dummy(self, a, b):
        return a + b

    def __str__(self):
        return "country: {:20} got {:.1f} totally.".format(self.country, self.total())

    def ToString(self):
        return print(self)

    def __repr__(self):
        # for developer to show Data Type with its members
        # if __str__ exists, it uses the __str__ first
        # this sample returns tuple in repr() function
        return "{}{}".format(self.__class__.__name__,
                             repr((self.country, self.gold, self.silver, self.bronze)))


class Athlete:
    def __init__(self) -> None:
        pass
