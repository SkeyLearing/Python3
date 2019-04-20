# 如何实现迭代对象和迭代器对象
import requests

from collections import Iterable, Iterator

'''
原理：
    Python的可迭代对象：字符串，列表
    由可迭代对象得到迭代器对象
    迭代对象接口：
        列表可迭代的接口：l.__iter__
        字符串可迭代接口：s.__getitem__
    迭代器对象接口：
        迭代器对象接口只有一个 t.next() ：
            t = iter(l)
            t.__next__()
    那么对于 for 循环进行迭代时，工作原理：
        for x in l:
            prit(x)
        先生成一个 iter(l) 的迭代器，接着调用 next() 接口，直至出现 StopIteration 异常，结束for循环。
'''

'''
实现步骤：
    1. 实现一个迭代器对象，next方法每次返回一个数据，迭代完毕抛出 StopIteration 异常。
    2. 实现一个可迭代对象， __iter__ 方法返回一个迭代器对象。
'''
# 示例：

# 先实现迭代器


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities        # 构造城市列表
        self.index = 0              # 初始索引值

    def get_weather(self, city):        # 获取城市天气数据
        r = requests.get(r"http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def __next__(self):             # 迭代器接口的作用，每次返回一个城市天气查询结果；城市信息查询完毕，抛出异常
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


# 迭代对象
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)     # 迭代对象的__iter__()方法返回的是一个迭代器对象。


if __name__ == '__main__':
    city_list = ['北京', '上海', '广州', '武汉']
    for x in WeatherIterable(city_list):
        print(x)
