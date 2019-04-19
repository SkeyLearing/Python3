from random import randint

'''
    根据字典中值的大小进行排序
    ·使用zip()函数将字典数据转化为元祖
    ·传递sorted函数的key参数
'''


d = {x: randint(60, 100) for x in 'xyzabc'}
t = zip(d.values(), d.keys())
print("zip()转化排序：", sorted(t))

print("sorted key 参数排序：", sorted(d.items(), key=lambda x: x[1]))