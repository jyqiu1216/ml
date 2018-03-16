# -*- coding: utf-8 -*-
from sklearn import tree

feature = [[178, 1], [155, 0], [177, 0], [165, 0], [169, 1], [160, 0]]

lable = ['male', 'female', 'male', 'female', 'male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(feature, lable)

print(clf.predict([[158, 0], [182, 1], [150, 1]]))
