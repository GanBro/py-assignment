import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
def runplt(size=None):
    plt.figure(figsize=size)
    plt.title('匹萨价格与直径数据',fontproperties=font)
    plt.xlabel('直径（寸）',fontproperties=font)
    plt.ylabel('价格（元）',fontproperties=font)
    plt.axis([0, 25, 0, 25])
    plt.grid(True)
    return plt
plt = runplt()
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
plt.plot(X, y, 'k.')
# plt.show()

from sklearn import linear_model
import numpy as np
model = linear_model.LinearRegression()
model.fit(X, y)
print(model.intercept_)
print(model.coef_)
a = model.predict([[12]])
# a[0][0]
# print("预测一张12寸匹萨价格：{:.2f}".format(model.predict([[12]])[0][0]))

plt = runplt()
plt.plot(X, y, 'k.')
X2 = [[0], [10], [14], [25]]
model = linear_model.LinearRegression()
model.fit(X,y)
y2 = model.predict(X2)
plt.plot(X2, y2, 'g-')
plt.show()