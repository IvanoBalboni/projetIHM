import village as vil
import random as rand

class Map():
    def __init__(self, seed, player_num, width, height,
        ressourcesqty=[1,3,3,1], environment_mod=[4,2,2,1]):
        """
        seed            = number generating the map
        player_num      = number of players, they should have 6 settles possible (before environment)
        width, height   = map size
        ressourcesqty   = 2**[]  >> weigth in level of tile for map generation
        environment_mod = 2**mod >> weigth in type  of tile for map generation
                                    [plain, forest, lake, mountain]
        """
        self.seed            = seed
        self.player_num      = player_num
        self.width           = width
        self.height          = height

        self.ressourcesqty   = ressourcesqty.copy()
        self.environment_mod = environment_mod.copy()

        #0-3 plains // 4-7 forests // 8-11 lakes // 12-15 mountains
        # attributes represents the 4 different levels of each type of tiles
        self.attributes =  {0: (1, 0), 1: (2, 0), 2: (3, 0), 3: (4, 0),
                            4: (0, 1), 5: (1, 2), 6: (1, 3), 7: (2, 4),
                            8: (1, 0), 9: (1, 1),10: (2, 1),11: (2, 2),
                            12:(0, 0),13: (0, 1),14: (0, 1),15: (0, 2)}

        self.attributes_keys = list(self.attributes.keys())

        temp = 0
        self.cum_weights = []
        #generates a cumulative weights array for random.choices()
        # (1<<i)<<j is the weigth of the tile
        for i in self.environment_mod:
            for j in self.ressourcesqty:
                temp = temp + ( (1<<i)<<j )
                self.cum_weights.append(temp)
        #tiles is a matrix [[line] * column] >> tiles[0][1] >> value in line 0, column 1
        self.tiles = []
        #village_attribution = {villageid: playerid} a village gets a player, can change the player controlling the village
        self.village_attribution = {}
        #villages_list     = stores all village instances
        self.village_list        = [None for i in range(self.player_num)]




    def generate(self):
        #TODO: decent generation

        rand.seed(self.seed)

        self.tiles = [rand.choices( ( self.attributes_keys ), cum_weights = self.cum_weights, k = self.width) for k in range(self.height)]

        for i in range(self.player_num):
            #temp = vil.Village()
            self.village_list[i] = None


if __name__ == "__main__":
    test = Map(1234, 10, 10, 3)
    test.generate()
    print(test.tiles)
    print(test.tiles[0][1])
