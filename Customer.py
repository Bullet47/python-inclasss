class Customer:
    def __init__(self):
        self.amount = 0  # 累计消费
        self.discount_reached = False
        self.real_amount = 0  # 判断是否累计100元
        self.discounted_i = 0  # 折扣了几次

    def addPurhase(self, amount):
        self.discountReached()  # 检测是否累计到100元
        self.amount += amount
        self.real_amount += amount
        if self.discount_reached:
            print("本次消费%d元，当前累计消费了%d元,此次消费折扣了%d元\n" % (amount, self.amount, 10), end="")
            self.discount_reached = False
        else:
            print("本次消费%d元,顾客当前累计消费了%d元\n" % (amount, self.amount), end="")

    def discountReached(self):
        if self.real_amount >= 100:
            self.discount_reached = True
            self.real_amount = 0
            self.discounted_i += 1

    def show_details(self):
        print("顾客累计消费了%d元，累计折扣了%d元，实际消费了%d元" % (
            self.amount, self.discounted_i * 10, (self.amount - self.discounted_i * 10)))


if __name__ == '__main__':
    customer = Customer()
    customer.addPurhase(100)
    customer.addPurhase(95)
    customer.addPurhase(5)
    customer.addPurhase(50)
    customer.show_details()
