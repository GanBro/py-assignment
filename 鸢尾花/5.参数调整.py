from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=10)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
# print("X_train:{}".format(X_train[:10]))
# print("y_train:{}".format(y_train[:10]))

Xnew=[[5, 2.9, 1, 0.2]]
prediction=knn.predict(Xnew)
print("Prediction:{}".format(prediction))
print("Predictedtargetname:{}".format(iris_dataset['target_names'][prediction]))




