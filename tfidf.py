__author__ = 'Tim'

from sklearn.feature_extraction.text import TfidfVectorizer
import data

list_recipe = data.Data()
list_ingredient = list_recipe.get_ingredients()
sub_list = list_ingredient
#print(sub_list)
recipe_in_sentence = list()

vectorizer = TfidfVectorizer(min_df=1,token_pattern='%(.[^%]*)%')
for recette in sub_list:
    str = "%"
    str = str + ('%%'.join(recette)) + str
    recipe_in_sentence.append(str)

print(sub_list[1])
print(sub_list[2])
#print(recipe_in_sentence)
X = vectorizer.fit_transform(recipe_in_sentence)
print(X.toarray())

