import threading

import time

from queue import Queue

class ThreadQueue:

    def job(self, l, q):
        for i in range(len(l)):
            l[i] = l[i]**2
        # return l
        q.put(l)        # 将计算结果存放到队列中

    def multithreading(self):
        q = Queue()     # 因多线程不能返回值，所以需要队列来存放返回值 替代return功能
        threads = []
        data = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
        for i in range(4):      # 创建4个线程，对data中的数据分别进行运算
            t = threading.Thread(target=self.job, args=(data[i], q))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()       # 等待所有线程运行完毕
        results = []
        for _ in range(4):
            results.append(q.get())     # 线程运行结束，从队列中取出计算结果
        print(results)


if __name__ == '__main__':
    T = ThreadQueue()
    T.multithreading()