import pickle
from data_cleaning import data_cleaning
from training import machine_learning
from picklechecker import picklechecker


class main:
    def __init__(self):
        self.data_cleaning = data_cleaning
        self.machine_learning = machine_learning
        self.X_cleaned = []
        self.y_cleaned = []
    
    def cleanup_module(self):
        MAIN_DIR = './chatterbot'
        OUT_DIR = './outputfiles_debug'
        dc = self.data_cleaning(MAIN_DIR,OUT_DIR)
        self.X_cleaned,self.y_cleaned = dc.__main__()
        pc = picklechecker("X_cleaned",self.X_cleaned)
        pc.save_pickle()
        pc = picklechecker("y_cleaned",self.y_cleaned)
        pc.save_pickle()
          

    def chatbot_module(self):
        ml = self.machine_learning(self.X_cleaned,self.y_cleaned)
        ml.__main__()


def __main__():
    startExec = main()
    checkpickles = ['X_cleaned','y_cleaned']
    for x in checkpickles :
        pc = picklechecker(x,"")
        if(pc.check_pickle() == False):
            startExec.cleanup_module()
        else:
            if(x == 'X_cleaned'):
                startExec.X_cleaned = pc.load_pickle()
            elif(x == 'y_cleaned'):
                startExec.y_cleaned = pc.load_pickle()

    startExec.chatbot_module()
    

if __name__ == "__main__":
    __main__()


        
        

