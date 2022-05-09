import math
import time


class Cannonball:
    def __init__(self, pos_x):
        self.pos_x = pos_x
        self.pos_y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.flight_time = 0

    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y

    def shoot(self, theta, v):
        self.speed_x = v * math.cos(theta)
        self.speed_y = v * math.sin(theta)
        self.move(0.01)
        time.sleep(0.1)  # 每隔0.1秒调用一次move函数
        while self.pos_y > 0:
            self.move(0.1)
            time.sleep(0.1)  # 每隔0.1秒调用一次move函数
        print("即%.1f秒后,炮弹近似落在地上，此时炮弹坐标为： x: %.4f y:%.4f" % (self.flight_time, self.getX(), self.getY()), end="")

    def move(self, sec):
        self.flight_time += sec
        self.pos_x += self.speed_x * sec
        self.pos_y += self.speed_y * sec
        self.speed_y -= 9.81 * sec
        print("%.1f秒后，炮弹坐标为： x: %.4f y:%.4f" % (self.flight_time, self.getX(), self.getY()))


if __name__ == '__main__':
    pos_x = float(input("请输入炮弹初始x坐标：  "))
    theta = float(input("请输入发射角度：  "))
    v = float(input("请输入初始速度：  "))
    cannonball = Cannonball(pos_x)
    cannonball.shoot((theta / 180) * math.pi, v)
