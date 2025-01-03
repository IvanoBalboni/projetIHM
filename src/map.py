import village as vil
import random as rand

TOPLEFT  = (-1, -1)
TOP      = ( 0, -1)
TOPRIGHT = ( 1, -1)
LEFT     = (-1, 0 )
RIGHT    = ( 1, 0 )
BOTLEFT  = (-1, 1 )
BOT      = ( 0, 1 )
BOTRIGHT = ( 1, 1 )

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
        #           list of lines
        self.tiles = []

        #villages_dict = stores all villages with format {id: ((x,y), playerid, adress)}
        self.village_dict = {}


    def generate(self):
        #TODO: decent generation

        rand.seed(self.seed)

        self.tiles = [rand.choices( ( self.attributes_keys ),
            cum_weights = self.cum_weights, k = self.width) for k in range(self.height)]


        ratio    = self.width  / self.height
        #number of columns to divide the map for spreading players
        row      = int( self.player_num // ratio )
        #number of rows to divide the map for spreading players
        col      = int(self.player_num // row + (self.player_num%ratio != 0) )
        x_section= self.width // col
        y_section= self.height // row

        #print(ratio, col, row, x_section, y_section)

        #generates a list of spawn points in the right col x row
        poslist  = [(rand.randint(x_section*(i%row)+1, x_section*(i%row)+x_section-2),
                    rand.randint(x_section*(i//row)+1, x_section*(i//row)+x_section-2)
                    )for i in range(col * row - 1)]
        #print(poslist)
        rand.shuffle(poslist)

        for i in range(self.player_num):
            x, y = poslist[i][0], poslist[i][1]
            self.village_dict[i] = ((x,y), i, vil.Village( self.get_all_neighbours(x,y) ))

    def get_cell_values(self, x, y, pos=(0,0)):
        return self.attributes[ self.tiles[x+pos[0]][y+pos[1]] ]

    def get_all_neighbours(self, x, y):
        #TODO: verif qu'il y ait pas d'inversion bizarre
        #print(x, y)
        out = [self.get_cell_values(x, y, TOPLEFT), self.get_cell_values(x, y, TOP), self.get_cell_values(x, y, TOPRIGHT),
               self.get_cell_values(x, y, LEFT)   , self.get_cell_values(x, y)     , self.get_cell_values(x, y, RIGHT)   ,
               self.get_cell_values(x, y, BOTLEFT), self.get_cell_values(x, y, BOT), self.get_cell_values(x, y, BOTRIGHT)
               ]
        #print(out)
        return out


if __name__ == "__main__":
    test = Map(1234, 10, 100, 30)
    test.generate()
    print(test.tiles)
    print(test.tiles[2][0])
    print(test.village_dict)
