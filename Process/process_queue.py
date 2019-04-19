
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(100):
        res += i+i**2+i**3
    q.put(res)

if __name__ == '__main__':
    q = mp.Queue()      # 这里的队列方法是 multiprocessing 中自带的，使用方法和多线程中的一样
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)