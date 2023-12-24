from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

n_dots = 40
X = 5 * np.random.rand(n_dots, 1)
y = np.cos(X).ravel()
y += 0.2 * np.random.rand(n_dots) - 0.1
print(X, y)