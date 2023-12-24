import numpy as np
np.random.seed(42)
x = np.random.uniform(-3,3,size=100)
X = x.reshape(-1,1)
y = 0.5 * x +3 +np.random.normal(0,1,size=100)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
def PolynomialRegression(degree):
    return Pipeline([("poly",PolynomialFeatures(degree=degree)),
    ("std_scaler",StandardScaler()),("lin_reg",lin_reg)])
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=666)

from sklearn.metrics import mean_squared_error

poly20_reg = PolynomialRegression(degree=20)
poly20_reg.fit(X_train,y_train)

y20_predict = poly20_reg.predict(X_test)
mse=mean_squared_error(y_test,y20_predict)
# print(mse)

import matplotlib.pyplot as plt
X_plot = np.linspace(-3,3,100).reshape(100,1)
y_plot = poly20_reg.predict(X_plot)
plt.scatter(x,y)
plt.plot(X_plot,y_plot,color='r')#有序排序后绘制曲线
plt.axis([-3,3,-1,6])
# plt.show()

from sklearn.linear_model import Ridge
def RidgeRegression(degree,alpha):
    return Pipeline([("poly",PolynomialFeatures(degree=degree)),
                ("std_scaler",StandardScaler()),
                ("ridge_reg",Ridge(alpha=alpha))])
def plot_model(model):
        X_plot = np.linspace(-3,3,100).reshape(100,1)
        y_plot = model.predict(X_plot)
        plt.scatter(x,y)
        plt.plot(X_plot,y_plot,color='r')
        plt.axis([-3,3,-1,6])
        plt.show()
plot_model(poly20_reg)
ridge1_reg = RidgeRegression(20,0.0001)
ridge1_reg.fit(X_train,y_train)
y1_predict = ridge1_reg.predict(X_test)
print(mean_squared_error(y_test,y1_predict))
plot_model(ridge1_reg)