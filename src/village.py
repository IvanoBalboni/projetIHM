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
        taxes      > [commoner_taxes, noble_taxes] 
        food       > price of food = persons_nb / food
        wood       > needed for new constructions
        money      > needed for construction and city actions
                   > money taken by nobles % 
        ressources > [food_multiplier, wood_multiplier]
        """
        #04/12/24 Suggestion:
        """
        habitations > a person without habitation will lose hapiness fast
                    and see their life expectancy reduced
                    No impact on food consumption"""
        self.commoner_nb     = persons_nb[0]
        self.churchman_nb    = persons_nb[1]
        self.noble_nb        = persons_nb[2]
        self.persons_nb      = self.commoner_nb + self.churchman_nb + self.noble_nb
        
        self.commoner_taxes  = taxes[0]
        self.noble_taxes     = taxes[1]

        self.food            = food
        self.wood            = wood
        self.money           = money

        self.food_multiplier = ressources[0]
        self.wood_multiplier = ressources[1]
    
    def gen_villagers(self):
        """
        generate all the villagers

        """
        f_name       = open(NAMES)
        f_first_name = open(FIRST_NAMES)

        names        = f_name.readlines()
        first_names  = f_first_name.readlines()

        random.seed(self.persons_nb * self.wood_multiplier * self.food_multiplier)

        for i in range(self.commoner_nb):
            name       = first_names[random.random(FIRST_NAMES_NB)][:-1]
            name       = name + " " +names[random.random(NAMES_NB)][:-1]
            expectancy  = random.random(30, 100)

    
    def update(self):
        """

        """
            

        


    
