import person as per

class Commoner(per.Person):
    def __init__(self, name, age, expectancy, id, rank, mood=5, wealth=0, fed=5,food=5):
        """rank : value between 0 and 1
        0 : peasant
        1 : artisan"""
        self.rank = rank
        if rank == 0:
            per.Person(self, name, age, expectancy, id)
            self.prod = 2
        else:
            per.Person(self,name,age,expectancy,id, 5, 20)
            self.prod = 4
