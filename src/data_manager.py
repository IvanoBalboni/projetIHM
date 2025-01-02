import map
import events
import player_factory as pf

class Data:
    def __init__(self, file):
        #TODO: mieux avec settings
        self.file   = file
        self.map    = map.Map(727, 5, 100, 30)
        self.map.generate()
        self.events = events.Events()
        self.pf     = pf.Player_factory([self.map.village_dict[i][0] for i in range(5)], [0, 1, 2, 3, 4])
        pass
    
    def save(self):
        #TODO json et trucs oui
        pass
    
    def load(self):
        #TODO json et trucs oui
        pass
    
    def start(self):
        self.map = map.Map()
        self.players = pf.Player_factory()
        self.events = events.Events()


if __name__ == "__main__":
    test = Data("test")