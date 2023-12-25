import numpy as np
import matplotlib.pyplot as plt

# 生成x的值，使用linspace
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 计算对应的sin(x)值
y_values = np.sin(x_values)

# 绘制正弦函数的曲线图
plt.plot(x_values, y_values, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('正弦函数 sin(x) 的曲线图')
plt.legend()
plt.grid(True)
plt.show()
