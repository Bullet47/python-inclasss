import threading
import time

lock_1 = threading.Semaphore(1)  # 检查售票员是否关门
lock_2 = threading.Semaphore(0)  # 检查司机是否停车


def 司机():
    for i in range(3):
        lock_1.acquire()
        print('司机开车')
        time.sleep(1)
        print('驾驶')
        print('到站停车')

        lock_2.release()


def 售票员():
    for i in range(3):
        lock_2.acquire()
        time.sleep(1)
        print('打开车门')
        print('乘客上下车')
        time.sleep(1)
        print('关上车门')

        lock_1.release()


if __name__ == '__main__':
    p1 = threading.Thread(target=司机)
    p2 = threading.Thread(target=售票员)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

'''
1.里面的lock_1,lock_2为两个信号量；

2.lock_1.acquire()为P操作，lock_1.release()为V操作；

3.lock_1 = threading.Semaphore(1)的意思是将信号量lock_1的初值赋为1。

注意：
Semaphore管理一个内置的计数器， 
每当调用acquire()时内置计数器-1； 
调用release() 时内置计数器+1； 
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。

我们将lock_1的初值赋为1，lock_2的初值赋为0，则先执行司机这一线程。
'''

