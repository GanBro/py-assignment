from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.uniform(-3,3,size=100)
X = x.reshape(-1,1)
y = 0.5 * x +3 +np.random.normal(0,1,size=100)
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=666)

def LassoRegression(degree,alpha):
    return Pipeline([("poly",PolynomialFeatures(degree=degree)),
                ("std_scaler",StandardScaler()),
                ("ridge_reg",Lasso(alpha=alpha))
            ])
lasso1_reg = LassoRegression(20,0.01)
lasso1_reg.fit(X_train,y_train)
y1_predict =lasso1_reg.predict(X_test)
print(mean_squared_error(y_test,y1_predict))