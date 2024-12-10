import tkinter as tk

class Popup:
    def __init__(self, root ,x, y, size_x, size_y):
        """
        opens a generic unmovable popup without borders
        it will adjust its position to always be visible (in our usecases)
        root           : window the popup must stay within
        x, y         : mouse position / popup position
        size_x, size_y : popup size, it will always fit the root (in our usecases)
        3 types : 
        lock       : the rest of the game can't be played 
                     until actions on the popup are made
        persistant : the popup doesn't lock the game but will
                     stay displayed as long as it is needed
        ephemeral  : the popup will disapear the moment a click
                     is made outside of it
        """
        self.root = root
    

    def natural_tile(self, x, y, type, territory, ressources):
        """
        ephemeral
        displays the type, territory it belongs to, and ressources of the tile.
        it has a button opening a vassal / stranger / enemy popup if it corresponds
        """
        pass
    
    def buildable_tile(self, x, y, type, territory, ressources, ):
        pass
    
    def village_tile(self, x, y, type, territory):
        pass

