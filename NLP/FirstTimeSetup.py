from data_cleaning import data_cleaning

class main:
    def __init__(self):
        self.data_cleaning = data_cleaning
        self.X_cleaned = []
        self.y_cleaned = []
        

    def cleanup_module(self):
        MAIN_DIR = './chatterbot'
        OUT_DIR = './outputfiles_debug'
        dc = self.data_cleaning(MAIN_DIR,OUT_DIR)
        self.X_cleaned,self.y_cleaned = dc.run_func()  



def __main__():
    startExec = main()
    startExec.cleanup_module()
     
    

if __name__ == "__main__":
    __main__()


        
        

