import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_data = requests.get(data_url).content.decode('utf-8')

# 解析数据
rows = raw_data.strip().split('\n')
data = []
for row in rows:
    data.append(list(map(float, row.strip().split())))

# 将数据转换为数组
data = np.array(data)
X = data[:, :-1]  # 特征
y = data[:, -1]   # 目标变量

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

# 创建决策树回归模型
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X_train, y_train)

# 在测试集上评估模型
y_pred = dt_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("测试集上的均方误差：", mse)

# 在训练集上评估模型
train_score = dt_reg.score(X_train, y_train)
print("训练集上的模型得分：", train_score)
