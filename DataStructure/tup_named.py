from random import randint
from collections import namedtuple
'''
    元祖元素命名，提高程序可读性
    ·定义类似其他语言的枚举类型，也就是定义一系列的数值常量
    ·使用标准库中的 collections.namedtuple 代替内置tuple
'''
# 枚举示例：

NAME, SEX, EMAIL, AGE = range(4)
student = ('jame', 'male', 'jame@admin.com', 18)
print("枚举类型：", student[NAME])

# 内置示例：
Stu = namedtuple('Student', ['name', 'sex', 'email', 'age'])

# 创建元祖

s = Stu('Tom', 'male', 'Tom@qq.com', '16')  # 位置传参
s2 = Stu(name='jerry', sex='male', email='jerry@qq.com', age=19)    # 关键字传参
print("内置一：", s.name)
print("内置二：", s2.name)