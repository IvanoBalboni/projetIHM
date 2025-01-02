class Events():
    '''
    Contient tout les evenements sur la carte et comment le
    '''
    def __init__(self):
        #{"<event name>" : weight (probability)}
        self.event = {
            "fire" : 1, "drought" : 2, "abundance" : 2,
            "war"  : 0
        }
        #list of event keys
        self.event_list = []
    

    def pick_event(self):
        #get random event yes
        pass
    
    def add_event(self, event):
        if event in self.event.getkeys():
            self.event_list.append[event]
        else:
            raise Exception("Events > failed to add event ", event)
