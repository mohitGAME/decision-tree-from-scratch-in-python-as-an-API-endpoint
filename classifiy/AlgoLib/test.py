import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split

from id3_decisiontree import DecisionTree


def accuracy (y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


data = datasets.load_breast_cancer()
training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

training_data = pd.DataFrame(training_data,  columns=[
                             'cOLOR', 'Size', 'Liability'])

dataset = pd.read_csv('Social_Network_Ads.csv')
# dataset = pd.read_csv('Book1.csv')


X = dataset[['Age', 'EstimatedSalary']].values
# print("1")
# print(M)
# X = dataset.iloc[:, [2, 3]].values
# print("2")
# print(X)
y = dataset.iloc[:, 4].values

# X = training_data.iloc[:, 0:2].values
# y = training_data.iloc[:, -1].values

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234)

# cc = Decision_Node()
# cc

clf = DecisionTree(max_depth=100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

acc = accuracy(y_test, y_pred)

print("Accuracy:", acc)
