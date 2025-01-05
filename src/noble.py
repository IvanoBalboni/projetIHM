import person as per

class Noble(per.Person):
    def __init__(self, name, age, expectancy, id, mood=5, wealth=0, fed=5,food=5):
        """
        yes
        """
        per.Person.__init__(self, name, age, expectancy, id, mood, wealth, fed, food)

    def update(self):
        per.Person.update(self)
