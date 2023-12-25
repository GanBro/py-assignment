import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def my_function(x):
    return 2 * x**2 + 30 * x - 11.5

# 生成X的值，使用linspace
X = np.linspace(-1000, 1000, 1000)

# 计算相应的Y值
Y = my_function(X)

# 绘制函数图表
plt.plot(X, Y, label='Y = 2x^2 + 30x - 11.5')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('函数图表：Y = 2x^2 + 30x - 11.5')
plt.legend()
plt.grid(True)
plt.show()
