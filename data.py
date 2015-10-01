__author__ = 'chris'

import pandas as pd
from collections import Counter

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

    def get_ingredients(self):
        return self.data.ingredients

    def get_cuisine(self):
        return self.data.cuisine

    def get_index(self):
        return self.data.index

"""test = Data()
ingredient_list = list()


for i in test.data.ingredients:
    ingredient_list = ingredient_list + i

print(Counter(ingredient_list).most_common())"""


