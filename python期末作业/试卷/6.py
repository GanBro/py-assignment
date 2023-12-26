import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y_values = np.sin(x_values)

plt.plot(x_values, y_values, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('正弦函数 sin(x) 的曲线图')
plt.legend()
plt.grid(True)
plt.show()
