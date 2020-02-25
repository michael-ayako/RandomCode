import pickle
import os
class picklechecker:
    def __init__(self,loc,var):
        self.loc = "./savepickles/"+ loc
        self.var = var
    
    def save_pickle(self):
        with open(self.loc, 'wb') as pickle_file:
            pickle.dump(self.var, pickle_file)
    
    def load_pickle(self):
        pickle_in = open(self.loc,"rb")
        var = pickle.load(pickle_in)
        pickle_in.close()
        return var

