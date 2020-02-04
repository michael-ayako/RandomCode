#General imports
import logger
import sys
import os

class chatterbot:
    def main():
        mainlog = logger("General imports.....")
        
    if __name__== "__main__":
        main()




#logging.info("Configuring logger...")


"""
logging.info("General imports.....")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from tqdm import tqdm
import re
import json
#import sklearn as sk
import tensorflow as tf
from nltk import word_tokenize as tokenize
from nltk import WordNetLemmatizer as lemmatizer
logging.info("General imports complete.....")

#static variables
MAIN_DIR = './chatterbot/'
STORAGE = []
EDITED_STORAGE = []
JSON_DUMP_Q, JSON_DUMP_A = [] , []
X , y = [] , []

'''
Code reused from the website
geeksforgeeks.com
https://www.geeksforgeeks.org/logging-in-python/
'''


#Fetching data from files and storing it in a variable LOLS!
def fetching_files():
    logging.info("Fetching data from files and storing it in a variable LOLS!.....")
    files = list(os.listdir(MAIN_DIR))
    for x in tqdm(files):
        fetchfile = open(str(MAIN_DIR+"/"+x))
        for x in fetchfile:
            STORAGE.append(x)
    logging.info("Data stored.....")

    
#Removing unnecessary data
def cleaning_data():
    logging.info("Removing unnecessary data.....")
    for x in tqdm(STORAGE):
        if(re.search("- -",x) or re.search("  -",x)  ):
            EDITED_STORAGE.append(x)


#Creating a dump file to match questions to responses
def dump_creation():
    logging.info("Creating a dump file to match questions to responses.....")
    q = ''
    for v in tqdm(EDITED_STORAGE):
        if re.search("- -",v):
            q = v
        if re.search("  -",v):
            JSON_DUMP_Q.append(re.sub("- -","",q.rstrip()))
            JSON_DUMP_A.append(re.sub("  -","",v.rstrip()))  
    logging.info("Data created created successfully....")   


#Tokenizing the words using NLTK
def tokenization():
    logging.info("Tokenization started........")     
    for x in JSON_DUMP_Q:
        X.append(tokenize(x))
    for x in JSON_DUMP_A:
        y.append(tokenize(x))
    logging.info("Tokenization successful...........")  

#Lematizing the words
def lematization():
    logging.info("Lematizing started.....")
    logging.info("Lematizing the data successful")

def rm_stopwords():
    logging.info("Removing stopwords started.....")
    logging.info("Removing stopwords successful")




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

"""