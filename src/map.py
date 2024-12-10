import village as vil
import random as rand

class Map():
    def __init__(self, seed, players,   
        width, height, plain_mod=4, forest_mod=2, lake_mod=2, mountain_mod=1):
        """
        seed            = number generating the map
        players         = number of players, they should have 6 settles possible (before environment)
        width, height   = map size
        environment_mod = 2**mod >> weigth in map generation
        """
        self.seed         = seed
        self.players      = players
        self.width        = width
        self.height       = height
        self.plain_mod    = plain_mod
        self.forest_mod   = forest_mod
        self.lake_mod     = lake_mod
        self.mountain_mod = mountain_mod

        #0-3 plains // 4-7 forests // 8-11 lakes // 12-15 mountains
        # attributes represents the 4 different state of type of tiles
        self.attributes   ={0: (1, 0), 1: (2, 0), 2: (3, 0), 3: (4, 0),
                            4: (0, 1), 5: (1, 2), 6: (1, 3), 7: (2, 4),
                            8: (1, 0), 9: (1, 1),10: (2, 1),11: (2, 2), 
                            12:(0, 0),13: (0, 1),14: (0, 1),15: (0, 2)}


        #village_attribution = {villageid: playerid} a village gets a player, can change the player controlling the village
        self.village_attribution = {}
        #villages_list     = stores all village instances
        self.village_list        = []




    

    def generate(self):
        #TODO: decent generation

        rand.seed(self.seed)

        for i in range(self.width):
            for j in range(self.height):


        
        for i in range(self.players):
            temp = vil.Village()
            self.villages[i] = 