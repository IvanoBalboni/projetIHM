import random 

import commoner
import churchman
import noble


NAMES          = "../data/names.txt"
FIRST_NAMES    = "../data/first-names.txt"
NAMES_NB       = 21985
FIRST_NAMES_NB = 4945

class Village():
    def __init__(self, persons_nb, habitations, taxes, food, wood, money, ressources):
        """
        persons_nb > [commoner_nb, churchman_nb, noble_nb]
        habitations> a person without habitation will lose hapiness & food FAST TODO: determine values
        taxes      > [peasant_taxes, ,artisan_taxes, noble_taxes]
        food       > price of food = persons_nb / food
        wood       > needed for new constructions
        money      > needed for construction and city actions
                   > money taken by nobles %
        ressources > [(food_multiplier, wood_multiplier),] *9
        """
        #04/12/24 Suggestion:
        """
        habitations > a person without habitation will lose hapiness fast
                    and see their life expectancy reduced
                    No impact on food consumption"""
        self.peasant_nb    = persons_nb[0]
        self.artisan_nb = persons_nb[1]
        self.churchman_nb    = persons_nb[2]
        self.noble_nb        = persons_nb[3]
        self.persons_nb      = self.peasany_nb + self.artisan_nb + self.churchman_nb + self.noble_nb

        self.peasant_taxes  = taxes[0]
        self.artisan_taxes = taxes[1]
        self.noble_taxes     = taxes[2]

        self.food            = food
        self.wood            = wood
        self.money           = money

        self.food_multiplier = ressources[0][0]
        self.wood_multiplier = ressources[0][1]

    def gen_villagers(self):
        """
        generate all the villagers

        """
        f_name       = open(NAMES)
        f_first_name = open(FIRST_NAMES)

        names        = f_name.readlines()
        first_names  = f_first_name.readlines()

        random.seed(self.persons_nb * self.wood_multiplier * self.food_multiplier)

        for i in range(self.artisan_nb):
            name       = first_names[random.random(FIRST_NAMES_NB)][:-1]
            name       = name + " " +names[random.random(NAMES_NB)][:-1]
            expectancy  = random.random(30, 100)
            rank = 1
            age = random.random(15,expectancy-5)
            commoner.Commoner(self, name, age, expectancy, i, rank)

        for j in range(i,self.peasant_nb+i):
            name       = first_names[random.random(FIRST_NAMES_NB)][:-1]
            name       = name + " " +names[random.random(NAMES_NB)][:-1]
            expectancy  = random.random(30, 70)
            rank = 0
            age = random.random(15,expectancy-5)
            commoner.Commoner(self,name,age,expectancy,j,rank)



    def update(self):
        """
        compare nb_persons to habitation and reduce mood and expectancy the an amount of persons
        equal to the difference (target peasants in priority)
        """


