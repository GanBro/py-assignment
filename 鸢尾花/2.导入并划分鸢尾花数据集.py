from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)

Xnew = ([[5, 2.9, 1, 0.2]])
prediction = knn.predict(Xnew)
# print("Prediction: {}".format(prediction))
# print("Prediction: {}".format(iris_dataset['target_names'][prediction]))

print("Test set score:{}".format(knn.score(x_test, y_test)))
