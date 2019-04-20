'''
    使用生成器函数实现可迭代对象
    生成器函数：包含 yield 语句的函数, 生成器对象也是一个可迭代对象

    实现一个可迭代对象的类，它能迭代出给定范围内所有的素数
    实现方法：
        将该类的__iter__方法实现生成器函数，每次 yield 返回一个素数
'''


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_primenum(self, k):
        if k < 2:
            return False

        for i in range(2, k):
            if k % i == 0:
                return False

        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.is_primenum(k):
                yield k


if __name__ == '__main__':
    for i in PrimeNumbers(1, 10):
        print(i)
