# 迭代器与迭代器模型二
import requests
'''
    迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    字符串，列表或元组对象都可用于创建迭代器：
    任何实现了__iter__和__next__()方法的对象都是迭代器。__iter__返回迭代器自身，__next__返回容器中的下一个值

'''
# 依据上述理论实现 demo1 中的天气迭代器


class IteratorDemo():
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    # 重写 __iter__方法   说明有可以迭代的能力（ iterable）

    def __iter__(self):
        return self

    def get_weather(self, city):
        r = requests.get(r"http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    # 重写 __next__方法 说明是  迭代器 (iterator)

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


if __name__ == "__main__":
    t = IteratorDemo(['北京', '上海', '广州', '武汉'])
    for i in t:
        print(i)