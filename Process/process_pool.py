import multiprocessing as mp

'''
    利用 multiprocessing 的Pool方法创建一个进程池，并且可以规定使用几个核
    比如两个核：pool = mp.Pool(processes=2)
    再用 map() 函数将数据和函数进行映射
'''
def job(x):
    return x*x


def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))      # 放入很多个参数，自动进行进程分配
    print(res)

def multicore2():
    pool = mp.Pool()
    # res = pool.apply_async(job, (2,))       # 每次只能用一个进程进行一个参数的计算
    # print(res.get())
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]   # 列表中的迭代，实现 map() 的功能
    print([res.get() for res in multi_res])
if __name__ == '__main__':
    multicore()
    multicore2()