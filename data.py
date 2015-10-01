__author__ = 'chris'

import pandas as pd

class Data:
    PATH_TRAINING ="./train.json"
    PATH_TEST ="./test.json"


    def __init__(self,train=0):
        if train:
            self.data = pd.read_json(self.PATH_TEST)
        else:
            self.data = pd.read_json(self.PATH_TRAINING)

    def nb_recipe(self):
        return (len(self.data.index))




test = Data()
print(test.data.columns)
print(test.data.loc[0])
print("Nouveau test")
print(test.data.as_matrix(['cuisine']))
