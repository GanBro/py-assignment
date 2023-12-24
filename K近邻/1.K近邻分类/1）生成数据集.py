from sklearn.datasets._samples_generator import make_blobs
centers = [[-2, 2], [2, 2], [0, 4]]
X,y = make_blobs(n_samples=60, centers=centers, random_state=0, cluster_std=0.60)
print(X, y)