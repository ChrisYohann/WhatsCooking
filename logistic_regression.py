__author__ = 'Tim'
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
import tfidf
import data as dt

pipeline = Pipeline([
    ("select",dt.ge)
     tfidf,
     SGDClassifier(loss="log", n_iter=50, n_jobs=-1, class_weight="auto")
                     ])