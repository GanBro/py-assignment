import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def my_function(x):
    return 2 * x**2 + 30 * x - 11.5

X = np.linspace(-1000, 1000, 1000)

Y = my_function(X)

plt.plot(X, Y, label='Y = 2x^2 + 30x - 11.5')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('函数图表：Y = 2x^2 + 30x - 11.5')
plt.legend()
plt.grid(True)
plt.show()
