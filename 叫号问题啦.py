#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 脆香米打死你
# datetime： 2022/5/26 19:14 
# ide： PyCharm
# 信号量：seat=15（座位数）  number=0(号数)互斥信号量 mutex（取号） service=0(营业员服务)
# 顾客：
# P（mutex）
# 取号
# V（mutex）
# P(seat)//获取座位
# 等待叫号
# V(number)
# P(service)//获取服务
# V(seat)
# 获取服务
#
# 营业员：
# P(number)//叫号
# V(service)//为用户服务
import threading
import time

mutex = threading.Semaphore(1)  # 互斥信号量
seat = threading.Semaphore(15)  # 座位数
number = threading.Semaphore(0)  # 当前号数
service = threading.Semaphore(0)  # 营业员服务


def lord():
    mutex.acquire()
    print('老爷%s正在取号\n' % threading.currentThread().name)
    mutex.release()
    seat.acquire()  # 获取座位
    print('老爷%s等待叫号\n' % threading.currentThread().name)
    number.release()
    service.acquire()
    seat.release()
    print('老爷%s已经获得了服务\n' % threading.currentThread().name)
    time.sleep(0.1)


def good_service():
    while True:
        number.acquire()  # 叫号
        service.release()  # 提供服务
        print("小人正在好好的服务\n")
        time.sleep(0.1)


def append_thread():
    return threading.Thread(target=lord)


if __name__ == '__main__':

    threads = []
    small_p = threading.Thread(target=good_service)
    small_p.start()
    threads.append(small_p)
    for i in range(50):
        p = append_thread()
        p.start()
        threads.append(p)  # 添加到线程中
    for t in threads:
        t.join()
