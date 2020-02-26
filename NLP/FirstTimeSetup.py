from keras.models import load_model
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
        with open("savepickles\X_cleaned", 'wb') as pickle_file:
            pickle.dump(self.X_cleaned, pickle_file)
        with open("savepickles\y_cleaned", 'wb') as pickle_file:
            pickle.dump(self.y_cleaned, pickle_file)
          

    def training_module(self):
        ml = self.machine_learning(self.X_cleaned,self.y_cleaned)
        ml.__main__()


def __main__():
    startExec = main()
    #Loading pickels
    try:
        pickle_in = open("savepickles\X_cleaned","rb")
        startExec.X_cleaned  = pickle.load(pickle_in)
        pickle_in.close()
 
        pickle_in = open("savepickles\y_cleaned","rb")
        startExec.y_cleaned  = pickle.load(pickle_in)
        pickle_in.close()
    except:
        startExec.cleanup_module()
    #lading models
    try:
        model = load_model('savepickles\model.h5')
    except Exception as e:
        print(e)
        startExec.chatbot_module()
    

if __name__ == "__main__":
    __main__()


        
        

