import player

class Player_factory:
    def __init__(self, spawn_list, player_list):
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
            self.players[n] = player.Player([100, 50, 50], [x-1, y-1, x+1, y+1], i)
            n += 1
    
    def play():
        #TODO trucs
        pass

if __name__ == "__main__":
    test = Player_factory([(2,2),(10,10),(15,5)], [0, 1, 1])
    print(test.players)