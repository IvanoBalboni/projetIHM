import map
import player_factory as pf
import events
import data_manager as dm

#TODO: lien entre joueur territoire (villages +)
#TODO: generation carte, joueurs etc..

class Game:
    def __init__(self, savefile):
        self.data = dm.Data(savefile)
        self.pf = self.data.pf
        self.map = self.data.map
        self.events = self.data.events


if __name__ == "__main__":
    g = Game("coucou")
    