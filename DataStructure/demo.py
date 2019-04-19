from collections import OrderedDict
from collections import deque
import pickle

# 有序字典与双端循环队列


d = OrderedDict()   # 建立一个有序的字典

# 双端循环队列 与 配置项文件读取

q = deque([], 5) # 第一个参数表示初始值，第二个参数表示队列长度

'''
    当q队列中值的个数达到5个时，写入下一个值的同时会将第一个写入的值进行移除，
    从而实现最近5次的输入历史记录
'''
pickle.dump(q, open('history', 'w'))       # 存储队列信息到文件 'history'

# 当程序开始运行时，读取文件
pickle.load(open('history'))