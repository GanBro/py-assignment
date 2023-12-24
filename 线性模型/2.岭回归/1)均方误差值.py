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
print(mse)