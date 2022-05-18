#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 脆香米打死你
# datetime： 2022/5/16 20:54 
# ide： PyCharm
import random
import threading
import time

mutex = threading.Semaphore(1)  # 左边互斥信号量
wait = threading.Semaphore(0)  # 左边互斥信号量
chess = threading.Semaphore(1)
player = 0


# 改进，可以不player--
def play_chess():
    print('棋手%s到达活动中心\n' % threading.currentThread().name)
    global player
    mutex.acquire()
    player += 1
    if player % 2 == 1:
        mutex.release()
        wait.acquire()
        print('棋手%s正在下棋\n' % threading.currentThread().name)
        time.sleep(1)
        print('棋手%s下完棋了\n' % threading.currentThread().name)
    else:
        mutex.release()
        chess.acquire()
        wait.release()
        print('棋手%s正在下棋\n' % threading.currentThread().name)
        time.sleep(1)
        print('棋手%s下完棋了\n' % threading.currentThread().name)
        chess.release()


def append_thread():
    return threading.Thread(target=play_chess)


if __name__ == '__main__':

    threads = []
    for i in range(50):
        p = append_thread()
        p.start()
        threads.append(p)  # 添加到线程中
    for t in threads:
        t.join()
