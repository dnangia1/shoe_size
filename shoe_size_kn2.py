from sklearn import neighbors

#[height(cm),weight(kg),shoe size(cm)]

X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

clf = neighbors.KNeighborsClassifier(n_neighbors=2)
clf = clf.fit(X,y)

prediction = clf.predict([[190,70,40]])
print(prediction)

#output=female