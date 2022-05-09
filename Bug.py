class Bug:
    def __init__(self, initialPosition):
        self.initialPosition = initialPosition
        self.speed = 1

    def turn(self):
        self.speed *= -1
        if self.speed < 0:
            print("虫子转身，现在向左移动")
        else:
            print("虫子转身，现在向左移动")

    def move(self):
        self.initialPosition += self.speed
        if self.speed < 0:
            print("虫子向左移动1个单位，移动后位置为" + str(self.getPostion()))
        else:
            print("虫子向右移动1个单位，移动后位置为" + str(self.getPostion()))

    def getPostion(self):
        return self.initialPosition


if __name__ == '__main__':
    bug = Bug(0)  # 初始从0开始
    print("虫子起始位置为" + str(bug.getPostion()))
    bug.move()
    bug.move()
    bug.turn()
    bug.move()
    bug.move()
