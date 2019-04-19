# 常用的数据解析
from random import randint

'''
    列表：随机生成10个 -10~10 之间的数，提取出正数
    ·过滤负数: filter() 与 列表解析
    ·列表解析的速度要高于 filter()
'''
list = [randint(-10, 10) for _ in range(10)]
print("filter函数：", filter(lambda x: x >= 0, list))
print("列表解析：", [x for x in list if x >= 0])

'''
    字典：随机生成20个学生的成绩，提取出大于90分的数据
    ·字典解析
'''
dict = {x: randint(60, 100) for x in range(1, 21)}
print("字典解析：", {k: v for k, v in dict.items() if v > 90})

'''
    集合：提取出能被3整除的数据
    ·集合解析
'''
coll = {-5, -3, 2, 5, 6, 7, 8, 9}
print("集合解析：", {x for x in coll if x % 3 == 0})