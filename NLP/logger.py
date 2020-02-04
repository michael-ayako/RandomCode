import os

class Logger:
    def __init__(self, message):
        self.message = message

    def log(self):
        path = 'chatterbot.log'
        if(os.path.isfile(path)!= True):
            logging = open(path,'w')
            logging.write('+++++Start of file++++')
            logging.close
            



