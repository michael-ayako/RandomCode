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
        history = self.model.fit(self.X_train, self.y_train, 
                        epochs=30, 
                        batch_size=10,
                        validation_data=(self.X_val, self.y_val))
        print('\nhistory dict:', history.history)

        # Evaluate the model on the test data using `evaluate`
        print('\n# Evaluate on test data')
        results = self.model.evaluate(self.X_test, self.y_test, batch_size=128)
        print('test loss, test acc:', results)

        # Generate predictions (probabilities -- the output of the last layer)
        # on new data using `predict`
        print('\n# Generate predictions for 3 samples')
        predictions = self.model.predict(self.X_test[:6])
        print('predictions shape:', predictions.shape)
        
        

    def __main__(self):
        self.traintestsplit()
        self.model_defination()




    
