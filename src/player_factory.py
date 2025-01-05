import player

class Player_factory:
    def __init__(self, spawn_list: list, player_list: list, player_names: list, player_colors: list):
        '''
        spawn_list  = (x,y) pos village 1
        player_list = liste de int (0 = joueur, 1 = bot)
        '''
        #{id, adresse player}
        self.players = {}
        n = 0
        for i in player_list:
            x = spawn_list[n][0]
            y = spawn_list[n][1]
            self.player_colors = player_colors
            self.players[n] = player.Player([500, 350, 350], [x-1, y-1, x+1, y+1], player_names[i], i)
            self.players[n].gain_territory([x,y, x+3, y+2])
            self.players[n].gain_territory([x-2,y-3, x, y])
            n += 1
    
    def play():
        #TODO trucs
        pass

if __name__ == "__main__":
    test = Player_factory([(2,2),(10,10),(15,5)], [0, 1, 1], ["bob", "toto", "titi"], ["red", "green", "blue"])
    print(test.players)