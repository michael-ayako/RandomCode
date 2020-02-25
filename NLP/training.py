from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split

class machine_learning:
    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.X_train,self.y_train,self.X_test,self.y_test,self.X_val,self.y_val = [],[],[],[],[],[]
        self.model = Sequential()
        
    def traintestsplit(self):
        self.X_train,self.X_test,self.y_train , self.y_test = train_test_split(self.X, self.y, test_size=0.25, random_state=42)

    def model_defination(self):
        x = self.X_train.shape[1]
        y = self.y_train.shape[1]
        self.X_val = self.X_train[-100:]
        self.y_val = self.y_train[-100:]
        self.X_train = self.X_train[:-100]
        self.y_train = self.y_train[:-100]
        self.model.add(Dense(12, input_dim=x, activation='softmax'))
        self.model.add(Dense(12, activation='softmax'))
        self.model.add(Dense(12, activation='softmax'))
        self.model.add(Dense(y, activation='softmax'))
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        
    
    def model_train(self):
        self.model.fit(self.X_train, self.y_train, 
            epochs=30, 
            batch_size=10,
            validation_data=(self.X_val, self.y_val))
        self.model.save("savepickles\model.h5")       
        

    def __main__(self):
        self.traintestsplit()
        self.model_defination()
        self.model_train()




    
