# 如何使用函数装饰器

# 将缓存功能写成一个装饰器


def cache_decor(func):          # 将斐波那契函数作为参数传递进来
    cache = {}

    def wrap(*args):            # 包裹函数，传入的参数应该与上述一致，但是不能保证每个参数函数都只有一个参数，所以这里采用 *args 收集参数的方式
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
# 原函数一


def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 原函数二:
#   一个共有10个台阶的楼梯，从下面走到上面，一次只能迈1~3个台阶，并且不能后退，计算走完这个台阶有多少种方法


@cache_decor
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count

# 需要添加一个缓存功能，让计算更加高效


def fibonacci_cache(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fibonacci_cache(n - 1, cache) + fibonacci_cache(n - 2, cache)
    return cache[n]


fibonacci = cache_decor(fibonacci)
print(fibonacci(50))
print(climb(10, (1, 2, 3)))