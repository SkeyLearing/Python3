import multiprocessing as mp

# 进程与线程的创建方法相同

def job(a, b):
    print("Add：", a+b)


if __name__ == '__main__':
    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    p1.join()
    print("All Done")