from itertools import islice        # 迭代器的切片操作

list = [x for x in range(20)]

list = iter(list)

# l1 = islice(list, 5, 10)       # 每次使用 islice 都需要重新申请迭代器对象
l2 = islice(list, 15, None)

# for i in l1:
#     print(i)

for x in l2:
    print(x)