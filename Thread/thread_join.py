import threading

import time

class ThreadJoin:

    def thread_one(self):
        print("T1 Start\n")
        for i in range(10):
            time.sleep(0.1)
        print("T1 Finish\n")

    def thread_two(self):
        print("T1 Start\n")
        print("T1 Finish\n")

    def run_thread(self):
        thread_one = threading.Thread(target=self.thread_one, name="T1")
        thread_two = threading.Thread(target=self.thread_two, name="T2")
        thread_one.start()
        thread_two.start()
        thread_one.join()       # join() 方法 等待之前的线程运行完毕之后再执行下面的代码
        thread_two.join()
        print("All Done")

if __name__ == '__main__':
    T = ThreadJoin()
    T.run_thread()