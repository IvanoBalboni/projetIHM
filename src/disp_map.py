import tkinter as tk

import disp_popup_factory as dpop
import player_factory as pf
import map as mp
import village as vil

PLAYER   = 0
NEUTRAL  = 1
VASSAL   = 2
STRANGER = 3
ENEMY    = 4

class DMap(tk.Canvas):
    def __init__(self, root, map: mp.Map, player_factory: pf.Player_factory):
        tk.Canvas.__init__(self, root, background="black")
        self.root = root

        self.map = map
        self.pf = player_factory

        self.scroll_x = 100 * self.map.width
        self.scroll_y = 100 * self.map.height
        self.configure(scrollregion=(0,0,self.scroll_x, self.scroll_y))

        self.tile_size = 100
        self.texture = ['lawn green','forest green', 'blue', 'grey']
        self.tile_name= ['plain', 'forest', 'lake', 'mountains']


        self.draw_tiles()
        self.draw_borders()

        self.current_player = 4#TODO:faire ca bien
                
        
        # move on the map with left click:
        self.pop = None
        self.bind("<ButtonPress-1>", self.scroll_start)
        self.bind("<B1-Motion>", self.scroll_move)

        self.village_keys = {}

        for k in self.map.village_dict.keys():
            self.village_keys[self.map.village_dict[k][0]] = k
        #print(self.village_keys)


    def draw_tiles(self):
        village_pos = [self.map.village_dict[k][0] for k in self.map.village_dict.keys()]
        size = self.tile_size
        xlen,ylen = len(self.map.tiles), len(self.map.tiles[0])

        for xp in range(xlen):
            for yp in range(ylen):
                tile = self.map.tiles[xp][yp]
                y = xp * self.tile_size
                x = yp * self.tile_size
                territory = self.check_territory(xp, yp)
                pos = str(xp) + "+" + str(yp)
                if (xp, yp) in village_pos:
                    #print("village")
                    temp = self.create_rectangle(x, y, x+size, y+size, fill="red",
                                              tags= ("tile", pos, "village", territory))
                else:
                    temp = self.create_rectangle(x, y, x+size, y+size, fill=self.texture[tile//4],
                                                tags= ("tile", pos, territory))
    
    def aquire(self,x,y):
        if self.pf.players[self.current_player].ressources[0] < 50:
            err = dpop.Popup(self.root, self.root.winfo_width(), self.root.winfo_height(),
                                x*100, y*100, 300, 200)
            err.error("not enough money")
            self.pop.destroy()
            return
        self.pf.players[self.current_player].gain_territory([y,x,y,x])
        self.pf.players[self.current_player].pay(50)
        pos = str(y) + "+" + str(x)
        temp = list(self.gettags(pos))
        temp[2] = self.pf.players[self.current_player].name
        temp = tuple(temp)
        self.itemconfig(self.find_withtag(pos)[0], tag = temp)
        self.pop.destroy()
        self.root.update_ressources()
        self.draw_borders()
    
    def construct(self,x,y):
        #print("hey")
        if self.pf.players[self.current_player].ressources[0] < 200 or (
            self.pf.players[self.current_player].ressources[1] < 150
            ) or self.pf.players[self.current_player].ressources[0] < 150:
            err = dpop.Popup(self.root, self.root.winfo_width(), self.root.winfo_height(),
                                x*100, y*100, 300, 200)
            err.error("not enough ressources")
            self.pop.destroy()
            return
        
        self.map.village_dict[len(self.map.village_dict)] = ((y, x),self.current_player,
                                                                vil.Village(self.map.get_all_neighbours(x,y)) ) 
        self.map.village_dict[len(self.map.village_dict)-1][2].generate()
        self.village_keys[(y,x)] = len(self.map.village_dict)-1
        self.pf.players[self.current_player].pay(200)
        self.pf.players[self.current_player].ressources[1] -= 150
        self.pf.players[self.current_player].ressources[2] -= 150
        self.pf.players[self.current_player].gain_territory([y-1,x-1,y+1,x+1])
        pos = str(y) + "+" + str(x)
        temp = list(self.gettags(pos))
        temp = [temp[0], temp[1], "village", temp[2]]
        temp = tuple(temp)
        self.itemconfig(self.find_withtag(pos)[0], tag = temp, fill="red")
        self.pop.destroy()
        self.root.update_ressources()
        self.draw_borders()
        #print(self.village_keys)
    
    def collect(self, pos):
        (x,y) = pos
        pos = (y,x)
        temp = self.map.village_dict[self.village_keys[pos]][2]

        self.pf.players[self.current_player].ressources[0] += temp.money
        self.pf.players[self.current_player].ressources[1] += temp.food
        self.pf.players[self.current_player].ressources[2] += temp.wood

        self.map.village_dict[self.village_keys[pos]][2].money -= temp.money
        self.map.village_dict[self.village_keys[pos]][2].wood -= temp.wood
        self.map.village_dict[self.village_keys[pos]][2].food -= temp.food
        self.root.update_ressources()



    
    def draw_borders(self):
        for p in self.pf.players:
            blist = self.border_list(self.pf.players[p])
            for b in blist:
                id = self.create_line(b[0]*self.tile_size, b[1]*self.tile_size, b[2]*self.tile_size, b[3]*self.tile_size,
                                  fill = self.pf.player_colors[p], width = 8)
                self.tag_raise(id)

    def check_territory(self, x, y):
        for p in self.pf.players.values():
            for ter in p.territory:
                if x >= ter[0] and y >= ter[1] and x <=ter[2] and y <= ter[3]:
                    return p.name
        return "neutral"
    
    def border_list(self, player):
        """
        generate the list of borders for a player
        """
        blist = []
        for ter in player.territory:
            y1, x1, y2, x2 = ter
            x2, y2 = x2+1, y2+1
            border = [x1, y1, x2, y1, "TOP"]
            blist.append(border.copy())

            border = [x2, y1, x2, y2, "RIGHT"]
            blist.append(border.copy())

            border = [x1, y2, x2, y2, "BOT"]
            blist.append(border.copy())

            border = [x1, y1, x1, y2, "LEFT"]
            blist.append(border.copy())
        #blist = self.merge_borders(blist)
        blist = self.trim_borders(blist)
        return blist
    
    def merge_borders(self, blist):
        """
        merge aligned touching borders
        """
        del_list = []
        for i in range(len(blist)):
            if i in del_list: continue
            curr = blist[i]
            for j in range(len(blist)):
                print(i,j)
                if j == i:continue
                print(i,j)
                b = blist[j]
                if curr[4] == b[4]:
                    if curr[0] == curr[2]:
                        if ( curr[1] >= b[1] and curr[1] <= b[3] ) or ( curr[3] >= b[1] and curr[3] <= b[3]):
                            temp = [ curr[1], curr[3], b[1], b[3]]
                            curr[1] = b[1] = min(temp)
                            curr[3] = b[3] = max(temp)
                            del_list.append(j)
                    else:
                        if ( curr[0] >= b[0] and curr[0] <= b[2] ) or ( curr[2] >= b[0] and curr[2] <= b[2]):
                            temp = [ curr[0], curr[2], b[0], b[2]]
                            curr[0] = b[0] = min(temp)
                            curr[2] = b[2] = max(temp)
                            del_list.append(j)
        i = 0
        for k in del_list:
            blist.pop(k-i)
            i += 1

        return blist
   
    def trim_borders(self, blist):
        """
        trim the border that overlaps
        """
        for curr in blist:
            vertical = curr[0] == curr[2]
            for b in blist:
                if vertical != (b[0] == b[2]):#only need to check perpendicular lines
                    match b[4]:
                        case "TOP":
                            if b[1] > curr[1] and b[1] < curr[3] and curr[0] > b[0] and curr[0] < b[2]:
                                curr[3] = b[1]
                                if curr[4] == "RIGHT":
                                    b[0] = curr[0]
                                else:
                                    b[2] = curr[0]
                        case "RIGHT":
                            if curr[1] > b[1] and curr[1] < b[3] and b[0] > curr[0] and b[0] < curr[2]:
                                curr[0] = b[0]
                                if curr[4] == "TOP":
                                    b[3] = curr[1]
                                else:
                                    b[1] = curr[1]
                        case "BOT":
                            if b[1] > curr[1] and b[1] < curr[3] and curr[0] > b[0] and curr[0] < b[2]:
                                curr[1] = b[1]
                                if curr[4] == "RIGHT":
                                    b[0] = curr[0]
                                else:
                                    b[2] = curr[0]
                        case "LEFT":
                            if curr[1] > b[1] and curr[1] < b[3] and b[0] > curr[0] and b[0] < curr[2]:
                                curr[2] = b[0]
                                if curr[4] == "TOP":
                                    b[3] = curr[1]
                                else:
                                    b[1] = curr[1]
        return blist


    
    def tileMenu(self, event):
        if self.pop is not None:
            self.pop.destroy()
        id = self.find_withtag("current")
        tags = self.gettags("current")
        #print(tags)
        if "tile" in tags:
            x, y, dump1, dump2 = self.coords(id)
            x, y = int(x//100), int(y//100)
            tile = self.map.tiles[y][x]
            if "village" in tags:
                self.pop = dpop.Popup(self.root, self.root.winfo_width(), self.root.winfo_height(),
                                event.x, event.y, 400, 600)
                self.pop.village_tile(self.map.village_dict[self.village_keys[(y,x)]][2],(x,y),tags[3])
            else:
                self.pop = dpop.Popup(self.root, self.root.winfo_width(), self.root.winfo_height(),
                                event.x, event.y, 200, 300)
                self.pop.natural_tile(self.tile_name[tile//4],(x,y),tags[2])
            self.pop.bind("<FocusOut>", self.pop.quit)
                
    
    def scroll_start(self, event):
        if self.pop is not None:
            self.pop.destroy()
        self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

if __name__ == "__main__":
    pass