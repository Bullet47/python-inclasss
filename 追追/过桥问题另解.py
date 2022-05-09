import random
import threading
import time

num = threading.Semaphore(2)  # 桥墩，临界资源
L = threading.Semaphore(1)  # 左边桥互斥信号量
R=threading.Semaphore(1)   #右边桥互斥信号量
南岸的人：
void ston(){
	P(num)
	P(S)
	通过桥南侧
	到达桥中间
	V(S)
	P(N)
	通过桥北侧
	V(N）
	V(num)
}
北岸的人：
void ntos(){
	P(num)
	P(N)
	通过桥北侧
	到达桥中间
	V(N)
	P(S)
	通过桥南侧
	V(S）
	V(num)
}


def L_R():
    num.acquire()
    L.acquire()
    print('行人%s已经通过桥左侧上桥墩，想要向右过桥\n' % threading.currentThread().name)
    time.sleep(5)
    mutex.acquire()
    print('行人%s从左向右过桥\n' % threading.currentThread().name)
    mutex.release()
    empty.release()


def R_L():
    empty.acquire()
    print('行人%s已经上桥墩，想要向左过桥\n' % threading.currentThread().name)
    time.sleep(5)
    mutex.acquire()
    print('行人%s从右向左过桥\n' % threading.currentThread().name)
    mutex.release()
    empty.release()


if __name__ == '__main__':

    threads = []
    for i in range(20):
        r = random.randint(0, 1)
        if r == 0:
            p = threading.Thread(target=L_R)
        else:
            p = threading.Thread(target=R_L)
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
