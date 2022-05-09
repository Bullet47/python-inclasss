import math
for ans in range(0, 10000):
    if int((ans + 100) ** 0.5) == math.ceil((ans + 100) ** 0.5):  # 它是完全平方数证明向上取整和向下取整都是同一个数,即没有小数
        if int((ans + 100 + 268) ** 0.5) == math.ceil((ans + 100 + 268) ** 0.5):
            print(ans)
