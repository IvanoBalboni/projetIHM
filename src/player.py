class Player():
    '''
    A player has ressources and territory, a bot is a player,
    A vassal bot is still a player but his actions will be reduced
    '''

    def __init__(self):
        pass

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
