#General imports
import sys
import os
import logging 
import json

logging.basicConfig(filename="outputfiles_debug/newfile.log", format='%(asctime)s %(message)s', filemode='w')  #Create and configure logger 
logging.info("Configuring logger...")
logger=logging.getLogger() #Creating an object 
logger.setLevel(logging.DEBUG) #Setting the threshold of logger to DEBUG 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from tqdm import tqdm
import re
import json
#import tensorflow as tf
from nltk import word_tokenize as tokenize
from nltk.stem import WordNetLemmatizer as lemmatizer
from nltk.corpus import stopwords 
import string

#static variables
MAIN_DIR = './chatterbot'
OUT_DIR = './outputfiles_debug'
STORAGE = []
EDITED_STORAGE = []
JSON_DUMP_Q, JSON_DUMP_A = [] , []
X_token , y_token = [] , []
X_lemma , y_lemma= [] , []
X_stop , y_stop= [] , []

def fetching_files():#Fetching data from files and storing it in a variable LOLS!
    files = list(os.listdir(MAIN_DIR))
    for x in tqdm(files):
        fetchfile = open(str(MAIN_DIR+"/"+x))
        for x in fetchfile:
            STORAGE.append(x.lower())
    F = open(str(OUT_DIR+"/STORAGE.ayx"),"w+")
    for x in STORAGE:
        F.write(x)
    F.close()

    

def cleaning_data():#Removing unnecessary data
    for x in tqdm(STORAGE):
        if(re.search("- -",x) or re.search("  -",x)  ):
            EDITED_STORAGE.append(x)
    F = open(str(OUT_DIR+"/EDITED_STORAGE.ayx"),"w+")
    for x in EDITED_STORAGE:
        F.write(x)
    F.close()
    



def dump_creation():#Creating a dump file to match questions to responses

    q = ''
    for v in tqdm(EDITED_STORAGE):
        if re.search("- -",v):
            q = v
        if re.search("  -",v):
            JSON_DUMP_Q.append(re.sub("- -","",q))
            JSON_DUMP_A.append(re.sub("  -","",v))  
    F = open(str(OUT_DIR+"/JSON_DUMP_Q.ayx"),"w+")
    for x in JSON_DUMP_Q:
        F.write(x)
    F.close()
    F = open(str(OUT_DIR+"/JSON_DUMP_A.ayx"),"w+")
    for x in JSON_DUMP_A:
        F.write(x)
    F.close()  


#Tokenizing the words using NLTK
def tokenization(): 
    for x in JSON_DUMP_Q:
        X_token.append(tokenize(x))
    for x in JSON_DUMP_A:
        y_token.append(tokenize(x))
    
    F = open(str(OUT_DIR+"/X_token.ayx"),"w+")
    for x in X_token:
        F.write(str(x))
    F.close()
    F = open(str(OUT_DIR+"/y_token.ayx"),"w+")
    for x in y_token:
        F.write(str(x))
    F.close()  


def lematization():#Lematizing the words
    lemm = lemmatizer()
    for x in X_token:
        X_lemma_temp = []
        for y in x:
            lema = lemm.lemmatize(y)
            X_lemma_temp.append(lema)
        X_lemma.append(X_lemma_temp)
    for x in y_token:
        y_lemma_temp = []
        for y in x:
            lema = lemm.lemmatize(y)
            y_lemma_temp.append(lema)
        y_lemma.append(y_lemma_temp)
    
    F = open(str(OUT_DIR+"/X_lemma.ayx"),"w+")
    for x in X_lemma:
        F.write(str(x))
    F.close()
    F = open(str(OUT_DIR+"/y_lemma.ayx"),"w+")
    for x in y_lemma:
        F.write(str(x))
    F.close() 

def rm_stopwords():
    stop_words = set(stopwords.words('english'))
    for x in X_lemma:
        X_stop_temp = []
        for y in x:
            if y not in stop_words and y not in string.punctuation:
                X_stop_temp.append(y)
        X_stop.append(X_stop_temp)
    for x in y_lemma:
        y_stop_temp = []
        for y in x:
            if y not in stop_words and y not in string.punctuation:
                y_stop_temp.append(y)
        y_stop.append(y_stop_temp)

    F = open(str(OUT_DIR+"/X_stop.ayx"),"w+")
    for x in X_stop:
        F.write(str(x))
    F.close()
    F = open(str(OUT_DIR+"/y_stop.ayx"),"w+")
    for x in y_stop:
        F.write(str(x))
    F.close() 

try:
    fetching_files()
    cleaning_data()
    dump_creation()
    tokenization()
    lematization()
    rm_stopwords()
except Exception as err:
    msg = str('Error: %s'%(err))
    print(msg)
    logger.error(err)

