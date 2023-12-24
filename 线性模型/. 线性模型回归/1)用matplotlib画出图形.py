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
plt.show()