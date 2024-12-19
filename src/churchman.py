import person as per

class Churchman(per.Person):
    """a churchman's gift is the village attribute that get boosted by the churchman"""
    def __init__(self, name, age, expectancy, id, mood=5, wealth=0, fed=5,food=5):
        gifts = ["happiness", "production", "wealth"] #different attributes that can be influenced by churchman
        per.Person.__init__(self, name, age, expectancy, id)
        self.gift=gifts[randint(0,3)] 

    def update(self):
        per.Person.update(self)
