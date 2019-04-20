
from itertools import chain

# 在for语句中迭代多个可迭代对象

# 并行迭代
# 示例：语数外成绩是三个列表， 进行并行迭代计算出每个人的总分
c = [80, 85, 90]
m = [82, 95, 99]
e = [65, 75, 85]
total = []
it = zip(c, m, e)
for c, m, e in it:
    total.append(c + m + e)
print(total)

# 串行迭代
# 示例：统计三个列表中大于90的数
c1 = [88, 94, 90]
m1 = [65, 80, 99]
e1 = [65, 93, 92]
to = []
for i in chain(c1, m1, e1):
    if i > 90:
       to.append(i)
print(to)