from sklearn.datasets import load_iris
iris_dataset = load_iris()

print(iris_dataset['target'])

print("--------------------------------------------")

print(iris_dataset['data'][:6])