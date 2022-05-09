import random
import threading

leftmutex = threading.Semaphore(1)  # 左边互斥信号量
rightmutex = threading.Semaphore(1)  # 左边互斥信号量
bridge = threading.Semaphore(1)
leftcount = 0
rightcount = 0


def L_R():
    print('行人%s等待从左到右过桥\n' % threading.currentThread().name)
    leftmutex.acquire()
    global leftcount
    leftcount += 1
    if leftcount == 2:  # 东侧第一个准备上桥的车去抢夺独木桥
        bridge.acquire()
    leftmutex.release()

    print('行人%s从左向右过桥\n' % threading.currentThread().name)

    leftmutex.acquire()
    leftcount -= 1
    if leftcount == 1:  # 东侧最后一个已经下桥的车去释放独木桥
        bridge.release()
    leftmutex.release()


def R_L():
    print('行人%s等待从左向右\n' % threading.currentThread().name)
    rightmutex.acquire()
    global rightcount
    rightcount += 1
    if (rightcount == 2):  # 东侧第一个准备上桥的车去抢夺独木桥
        bridge.acquire()
    rightmutex.release()
    print('行人%s从右向左过桥\n' % threading.currentThread().name)
    rightmutex.acquire()
    rightcount -= 1
    if rightcount == 1:  # 东侧最后一个已经下桥的车去释放独木桥
        bridge.release()
    rightmutex.release()


def append_thread():
    r = random.randint(0, 1)
    if r == 0:
        p = threading.Thread(target=L_R)
    else:
        p = threading.Thread(target=R_L)
    return p


if __name__ == '__main__':

    threads = []
    for i in range(50):
        p = append_thread()
        p.start()
        threads.append(p)  # 添加到线程中
    for t in threads:
        t.join()

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
