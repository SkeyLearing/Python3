
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):     # 正向迭代器
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):     # 反向迭代器
        t = self.end
        while t >= self.start:
            yield t
            t -= self.start


if __name__ == '__main__':
    for x in FloatRange(1, 10, 2):
        print(x)