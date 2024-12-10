import village as vil

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


        #village_attribution = {villageid: playerid} a village gets a player, can change the player controlling the village
        self.village_attribution = {}
        #villages_list     = stores all village instances
        self.village_list        = []




    

    def generate(self):
        #TODO: decent generation
        for i in range(self.players):
            temp = vil.Village()
            self.villages[i] = 