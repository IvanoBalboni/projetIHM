import map
import player_factory as pf
import events
import data_manager as dm

#TODO: lien entre joueur territoire (villages +)
#TODO: generation carte, joueurs etc..

class Game:
    def __init__(self, savefile):
        self.main_player = 4
        self.data: dm.Data = dm.Data(savefile) 
        self.pf: pf.Player_factory = self.data.pf 
        self.map: map.Map = self.data.map 
        self.events = self.data.events 


if __name__ == "__main__":
    g = Game("coucou")
    