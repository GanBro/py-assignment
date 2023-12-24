# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:51:58 2021

@author: lenovo
"""
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np
n_dots = 40
X = 5 * np.random.rand(n_dots, 1)
y = np.cos(X).ravel()
y += 0.2 * np.random.rand(n_dots) - 0.1

k = 5
knn = KNeighborsRegressor(k)
knn.fit(X, y)

# 生成足够密集的点并进行预测
T = np.linspace(0, 5, 500)[:, np.newaxis]
y_pred = knn.predict(T)
print(knn.score(X, y)) # 计算拟合曲线对训练样本的拟合准确性。

# 画出拟合曲线。

plt.figure(figsize=(5,3), dpi=144)
plt.scatter(X, y, c='g', label='train data', s=10) #画出训练样本
plt.plot(T, y_pred, c='k', label='prediction', lw=1) # 画出拟合曲线
plt.axis('tight')
plt.title('KNeighborsRegressor (k=%i)' % k)
plt.legend()
plt.savefig('knn_regressor.png')
plt.show()