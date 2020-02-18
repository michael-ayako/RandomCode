from sklearn.model_selection import train_test_split

class machine_learning:
    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.X_train,self.y_train,self.X_test,self.y_test = [],[],[],[]
        
    def traintestsplit(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.33, random_state=42)

    def __main__(self):
        self.traintestsplit()


    
