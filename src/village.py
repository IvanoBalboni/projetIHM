import random

import back_header as back

import commoner
import churchman
import noble

#int to access the adress on different lists matching the name
PEASANT   = 0
ARTISAN   = 1
CHURCHMAN = 2
NOBLE     = 3

class Village():
    def __init__(self, ressources, persons_nb=[10, 0, 0, 1], habitations=3,
                 taxes=[0.5, 0.25, 0, 0.125], food=50, wood=50, money=100):
        """
        ressources > tiles the village is on and will have access to as drawn bellow
                    [ TOPLEFT,   TOP  , TOPRIGHT ,
                      LEFT   , VILLAGE,   RIGHT  ,
                      BOTLEFT,   BOT  , BOTRIGHT ]
        persons_nb > [peasant_nb, artisan_nb, churchman_nb, noble_nb]
        habitations> a person without habitation will lose hapiness, food & expectancy quickly
                     1 habitation can host 5 persons, a noble takes 2 places
        taxes      > [peasant_taxes, artisan_taxes, churchman_taxes, noble_taxes]
        food       > food stored in the village persons can buy
                     price of food = persons_nb / food
        wood       > needed for new constructions
        money      > needed for construction and city actions
                     money taken by nobles %
        """

        self.ressources      = ressources.copy()
        self.persons_nb      = persons_nb.copy()
        self.persons_count   = sum(self.persons_nb)

        self.habitations     = habitations
        self.space           = habitations * 5
        self.hab_available   = True

        self.taxes           = taxes.copy()

        self.food            = food
        self.wood            = wood
        self.money           = money
        #At first only the village tile is usable, the multiplier will add up
        #when the access to more tiles is unlocked.
        self.food_multiplier = ressources[4][0]
        self.wood_multiplier = ressources[4][1]

        self.ressources = ressources.copy()

        #Generates the seed based on the ressources, it is possible to get
        #an identical village this way by luck or if the player knows how..
        #It isn't influenced by the map so an expert can maximise their chances
        #to get very good villages by placing it on a good seed spot
        self.seed = sum( (tile[0])*5 + tile[1] for tile in self.ressources ) * self.persons_count

        #Stores persons with the format id : adress, in either housed or homeless
        self.housed   = {}
        self.homeless = {}


    def generate(self):
        """
        generate all the villagers

        """
        f_name       = open(back.NAMES)
        f_first_name = open(back.FIRST_NAMES)

        names        = f_name.readlines()
        first_names  = f_first_name.readlines()

        random.seed(self.seed)

        #TODO: Noble
        #generates artisans
        for i in range(self.persons_nb[ARTISAN]):
            name       = first_names[random.randrange( back.FIRST_NAMES_NB)][:-1]
            name       = name + " " +names[random.randrange( back.NAMES_NB)][:-1]
            expectancy = random.randint( 30, 100)
            age        = random.randint( 15,expectancy-5)
            adress     = commoner.Commoner(name, age, expectancy, i, 1)
            if self.hab_available:
                self.housed[i] = adress
                self.space -= 1
                self.hab_available = self.space > 0
            else:
                self.homeless[i] = adress

        #generates peasants
        for j in range(self.persons_nb[ARTISAN], self.persons_nb[PEASANT] + self.persons_nb[ARTISAN]):
            name       = first_names[random.randrange( back.FIRST_NAMES_NB)][:-1]
            name       = name + " " +names[random.randrange( back.NAMES_NB)][:-1]
            expectancy = random.randint( 30, 70)
            age        = random.randint( 15,expectancy-5)
            adress     =commoner.Commoner(name, age, expectancy, j, 0)
            if self.hab_available:
                self.housed[j] = adress
                self.space -= 1
                self.hab_available = self.space > 0
            else:
                self.homeless[j] = adress
        #TODO: Noble



    def update(self):
        """
        TODO: proper update
        """

if __name__ == "__main__":
    test = Village([(2,2),(2, 2),(2, 2),
                    (2,2),(0, 2),(2, 2),
                    (2,2),(2, 2),(2, 2)])
    test.generate()
    for p in test.housed.values():
        print(p.name, p.age, p.expectancy)
