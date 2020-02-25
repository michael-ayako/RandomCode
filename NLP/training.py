from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from sklearn.model_selection import train_test_split

class machine_learning:
    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.X_train,self.y_train,self.X_test,self.y_test,self.X_val,self.y_val = [],[],[],[],[],[]
        self.model = keras.Model()
        
    def traintestsplit(self):
        self.X_train,self.X_test,self.y_train , self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def model_defination(self):
        

    def __main__(self):
        self.traintestsplit()
        print(len(self.X_test))
        print(len(self.y_test))
        self.model_defination()




    
