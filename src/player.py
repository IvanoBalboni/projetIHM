class Player():
    '''
    A player has ressources and territory, a bot is a player,
    A vassal bot is still a player but his actions will be reduced
    '''

    def __init__(self, ressources, territory, role):
        '''
        ressources > [money, food, wood]
        territory  > [(x1,y1,x2,y2)]
        role       > player or bot
        '''
        self.ressources = ressources
        self.territory  = []
        self.territory.append( territory.copy() )
        self.role = role


    def bot(self):
        '''
        The bot method defines a behaviour of 1 , it will
        execute actions like the player,
        all actions will be made in the Event_manager.
        The bot can't planify, it only makes decisions based
        on the current information available to it through
        the player class.
        The extended tutorial displays what actions a bot
        would have made.
        '''
    
    def __str__(self):
        ressources = "money: " + str(self.ressources[0]) + " food: " + str(self.ressources[1]) + " wood: " + str(self.ressources[2])
        out = ressources + " type: " + self.role
        return out

if __name__ == "__main__":
    test = Player([10, 0, 0], [0, 0, 5, 5], "player")
    print(test)