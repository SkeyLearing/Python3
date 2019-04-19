from random import randint
from collections import Counter

# 统计频度出现最高的三个数
'''
    将序列传入 Counter 的构造器，得到Counter对象时元素频度的字典
    Counter.most_common(n) 得到的时频度最高的n个元素
'''

seq = [randint(0, 20) for _ in range(30)]
c = Counter(seq)            # 得到元素频度字典
print("Counter:", c.most_common(3))     # 得到元素频度最高的3个元素