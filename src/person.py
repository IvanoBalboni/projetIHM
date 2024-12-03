class Person:
    def __init__(self, name, age, expetency, id, mood=5, wealth=0, fed=5,food=5):
        """
        1 food is consumed each turn, if food reaches 0, 1 fed is consumed each turn.
        a person will buy 1 food at the exchange rate after paying taxes. (managed in village)
        """
        self.age = age
        self.expetency = expetency
        self.id = id
        self.mood = mood
        self.wealth = wealth
        self.fed = fed
        self.food = food
        self.name = name
        self.alive = (life < expetency)
    
    def pay(self, ammount):
        self.wealth -= ammount
    
    def update(self):
        if self.food > 0 :
            self.food-= 1
        elif self.fed > 0 :
            self.fed -=1
        else:
            self.alive = False
    





    