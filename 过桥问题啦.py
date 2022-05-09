import random
import threading
import time

empty = threading.Semaphore(2)  # 桥墩，临界资源
mutex = threading.Semaphore(1)  # 过桥信号量


def L_R():
    print('行人%s等待上桥墩\n' % threading.currentThread().name)
    empty.acquire()
    print('行人%s已经上桥墩，想要向右过桥\n' % threading.currentThread().name)
    time.sleep(1)
    mutex.acquire()
    print('行人%s从左向右过桥\n' % threading.currentThread().name)
    mutex.release()
    empty.release()


def R_L():
    print('行人%s等待上桥墩\n' % threading.currentThread().name)
    empty.acquire()
    print('行人%s已经上桥墩，想要向左过桥\n' % threading.currentThread().name)
    time.sleep(1)
    mutex.acquire()
    print('行人%s从右向左过桥\n' % threading.currentThread().name)
    mutex.release()
    empty.release()


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
