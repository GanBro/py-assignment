from sklearn.datasets._samples_generator import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

centers = [[-2, 2], [2, 2], [0, 4]]
X,y = make_blobs(n_samples=60, centers=centers, random_state=0, cluster_std=0.60)

plt.figure(figsize=(5, 3), dpi=144)
center = np.array(centers)
plt.scatter(X[:,0], X[:,1], c=y, s=10, cmap='cool')
plt.scatter(center[:,0], center[:,1], s=50, marker='^', c='orange')
plt.savefig('knn_centers.png')
plt.show()

