from random import randint, sample
from functools import reduce

'''
    快速查找多个字典中的公共键
    ·Step1：使用字典的viewkeys()方法得到一个keys的集合
    ·Step2：使用map函数，得到所有字典的keys集合
    ·Step3：使用reduce函数，取得所有字典的keys的集合的交集 
'''

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s1.keys())
print(map(dict.keys, [s1, s2, s3]))
print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))

'''
    随机取样
    sample(序列a，n)
    功能：从序列a中随机抽取n个元素，并将n个元素生以list形式返回
'''

'''
    reduce函数，reduce函数会对参数序列中元素进行累积。
    reduce函数的定义：
        reduce(function, sequence [, initial] ) -> value
        function参数是一个有两个参数的函数，reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function。
        第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function，
        否则会以序列sequence中的前两个元素做参数调用function。
    
'''