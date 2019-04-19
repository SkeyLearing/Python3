import threading



class FirstKnowThread:

    def thread_job(self):
        print("这是新添加的线程：", threading.current_thread())

    def run_thread(self):
        added_thread = threading.Thread(target=self.thread_job, name='T1')   # 给线程进行命名
        added_thread.start()        # 启动线程
        added_thread.join()         # 等待
        # print("查看当前激活线程的数量：", threading.active_count())
        # print("查看当前的线程：", threading.enumerate())
        # print("当前运行的线程是：", threading.current_thread())


if __name__ == "__main__":
    T = FirstKnowThread()
    T.run_thread()
