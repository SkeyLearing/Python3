

import threading
'''
    假设有一个变量，需要等待线程一处理完毕之后，再由线程二进行使用，这个时候就需要用到锁
    两个线程同时去访问并改变 全局变量的时候 避免数据出错 给操作过程上一个 锁 
    即谁先到谁先处理处理数据 处理完成之后并释放数据 让其另一个线程进行数据处理
'''

def job1():
    global A, lock
    lock.acquire()  # 上锁
    for i in range(10):
        A += 1
        print("job1:", A)
    lock.release()  # 释放


def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print("job2:", A)
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()  # 生成一个锁
    A = 0  # 共享内存
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
