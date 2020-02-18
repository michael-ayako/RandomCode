#General imports
import sys
import os
import logging 
import json
import time
from tqdm import tqdm
import re
from nltk import word_tokenize as tokenize
from nltk.stem import WordNetLemmatizer as lemmatizer
from nltk.corpus import stopwords 
import string
from keras.preprocessing.text import one_hot
from keras.preprocessing.text import Tokenizer


logging.basicConfig(filename="outputfiles_debug/log_data.log", format='%(asctime)s %(message)s', filemode='w')  #Create and configure logger 
logging.info("Configuring logger...")
logger=logging.getLogger() #Creating an object 
logger.setLevel(logging.DEBUG) #Setting the threshold of logger to DEBUG 

class data_cleaning:
    def __init__(self,MAIN_DIR,OUT_DIR):
        self.MAIN_DIR = MAIN_DIR
        self.OUT_DIR = OUT_DIR
        self.STORAGE = []
        self.EDITED_STORAGE = []
        self.JSON_DUMP_Q, self.JSON_DUMP_A = [] , []
        self.X_token , self.y_token = [] , []
        self.X_lemma , self.y_lemma= [] , []
        self.X_stop , self.y_stop= [] , []
        self.X_bag , self.y_bag= [] , []

    def fetching_files(self):#Fetching data from files and storing it in a variable LOLS!
        files = list(os.listdir(self.MAIN_DIR))
        for x in tqdm(files):
            fetchfile = open(str(self.MAIN_DIR+"/"+x))
            for x in fetchfile:
                self.STORAGE.append(x.lower())
    
    def cleaning_data(self):#Removing unnecessary data
        for x in tqdm(self.STORAGE):
            if(re.search("- -",x) or re.search("  -",x)  ):
                self.EDITED_STORAGE.append(x)
        
    def dump_creation(self):#Creating a dump file to match questions to responses
        q = ''
        for v in tqdm(self.EDITED_STORAGE):
            if re.search("- -",v):
                q = v
            if re.search("  -",v):
                self.JSON_DUMP_Q.append(re.sub("- -","",q))
                self.JSON_DUMP_A.append(re.sub("  -","",v))  

    #Tokenizing the words using NLTK
    def tokenization(self): 
        for x in self.JSON_DUMP_Q:
            self.X_token.append(tokenize(x))
        for x in self.JSON_DUMP_A:
            self.y_token.append(tokenize(x))

    def lematization(self):#Lematizing the words
        lemm = lemmatizer()
        for x in self.X_token:
            X_lemma_temp = []
            for y in x:
                lema = lemm.lemmatize(y)
                X_lemma_temp.append(lema)
            self.X_lemma.append(X_lemma_temp)
        for x in self.y_token:
            y_lemma_temp = []
            for y in x:
                lema = lemm.lemmatize(y)
                y_lemma_temp.append(lema)
            self.y_lemma.append(y_lemma_temp)

    def rm_stopwords(self):
        stop_words = set(stopwords.words('english'))
        for x in self.X_lemma:
            X_stop_temp = []
            for y in x:
                if y not in stop_words and y not in string.punctuation:
                    X_stop_temp.append(y)
            self.X_stop.append(X_stop_temp)
        for x in self.y_lemma:
            y_stop_temp = []
            for y in x:
                if y not in stop_words and y not in string.punctuation:
                    y_stop_temp.append(y)
            self.y_stop.append(y_stop_temp)

    def bagofwords(self):
        X = Tokenizer()
        X.fit_on_texts(self.X_stop)
        self.X_bag = X.texts_to_matrix(self.X_stop, mode='count')
        y = Tokenizer()
        y.fit_on_texts(self.y_stop)
        self.y_bag = y.texts_to_matrix(self.y_stop, mode='count')

    def run_func(self):
        try:
            self.fetching_files()
            self.cleaning_data()
            self.dump_creation()
            self.tokenization()
            self.lematization()
            self.rm_stopwords()
            self.bagofwords()
            return (self.X_bag,self.y_bag)
        except Exception as err:
            msg = str('Error: %s'%(err))
            print(msg)
            logger.error(err)





