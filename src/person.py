class Person:
    def __init__(self, name, age, expectancy, id, mood=5, wealth=0, fed=5,food=5):
        """
        1 food is consumed each turn, if food reaches 0, 1 fed is consumed each turn.
        a person will buy 1 food at the exchange rate after paying taxes. (managed in village)
        """
        self.name = name
        self.age = age
        self.expectancy = expectancy
        self.id = id
        self.mood = mood
        self.wealth = wealth
        self.fed = fed
        self.food = food

        self.alive = self.age < self.expectancy

    def pay(self, ammount):
        self.wealth -= ammount

    def update(self):
        self.age += 1 #person age 1 year every turn

        if self.age >= self.expectancy:
            self.alive = False
            """
            a person may live 5 consecutive days without food
            regardless of wether or not they fasted in the past, the
            fed value is therefore being reset everytime food is consumed
            """
        elif self.food > 0:
            self.food -= 1
            self.fed = 5

        elif self.fed > 0:
            self.fed -= 1

        else:
            self.alive = False
