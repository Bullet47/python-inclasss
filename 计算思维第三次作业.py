import matplotlib.pyplot as plt
import numpy as np


def satlin(n):
    if n < 0:
        return 0
    if 0 <= n <= 1:
        return n
    if n > 1:
        return 1

def sss():
    print("这是乱写的")


def purelin(n):
    return n


if __name__ == '__main__':
    w111 = 2.0
    w121 = 1.0
    b11 = 2.0
    b12 = -1.0
    w211 = 1.0
    w212 = -1.0
    b21 = 0.0
    list_p = np.arange(-3, 3.1, 0.1)
    print(list_p)
    list_n11 = []
    for p in list_p:
        list_n11.append(w111 * p + b11)
    list_n12 = []
    for p in list_p:
        list_n12.append(w121 * p + b12)
    list_a11 = []
    for n11 in list_n11:
        list_a11.append(satlin(n11))
    list_a12 = []
    for n12 in list_n12:
        list_a12.append(satlin(n12))
    list_n21 = []
    for aii in range(0, len(list_a11)):
        list_n21.append(w211 * list_a11[aii] + w212 * list_a12[aii])
    list_a21 = []
    for n21 in list_n21:
        list_a21.append(purelin(n21))

    plt.figure()
    plt.plot(list_p, list_a11)
    plt.plot(list_p, list_a12, color='red', linestyle='--')
    plt.xlabel("p")
    plt.ylabel("$\mathregular{a^1}$")
    plt.title("$\mathregular{a^1}$-p")
    plt.legend(['$\mathregular{a^1_1}$ - p', '$\mathregular{a^1_2}$ - p'], loc='upper left')
    plt.savefig('a1-p.png')  # 保存图片
    plt.show()
    # 画n1-p
    plt.figure()  # 类似于先声明一张图片，这个figure后面所有的设置都是在这张图片上操作的
    plt.plot(list_p, list_n11)  # 制图
    plt.plot(list_p, list_n12, color='red', linestyle='--')  # 设置函数线的颜色和线的样式
    plt.xlabel("p")
    plt.ylabel('$\mathregular{n^1}$')
    plt.title("$\mathregular{n^1}$-p")
    plt.legend(['$\mathregular{n^1 _1}$ - p', '$\mathregular{n^1 _2}$ - p'], loc='upper left')
    plt.savefig('n1-p.png')  # 保存图片
    plt.show()
    # 画n21-p
    plt.figure()
    plt.plot(list_p, list_n21)
    plt.xlabel("p")
    plt.ylabel("$\mathregular{n^2_1}$")
    plt.title("$\mathregular{n^2_1}$-p")
    plt.savefig("n2-p.png")
    plt.show()
    # 画a21-p
    plt.figure()
    plt.plot(list_p, list_a21)
    plt.xlabel("p")
    plt.ylabel("$\mathregular{a^2_1}$")
    plt.title("$\mathregular{a^2_1}$-p")
    plt.savefig("a21-p.png")
    plt.show()
    n11 = (w111 * p + b11)
    n12 = (w121 * p + b12)
    a11 = satlin(n11)
    a12 = satlin(n12)
    n21 = w211 * a11 + w212 * a12  # [w211,w212]*[a11,a12](为列向量)
    a21 = purelin(n21)
