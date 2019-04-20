# 字符串操作
import re

# 如何分割含有多个分隔符的字符串

s = "1,2,3,56|897|,56,49;985;624;"

s1 = re.split(r"[,|;]+", s)

print(s1)

# 判断字符串a 是否以字符串b开头或者结尾
# startswith, endswith接收的参数必须是元祖
li = ['e.py', 'g.sh', 'd.java', 'a.cpp']

print("判断是否以 a, d 开头", [i for i in li if i.startswith(('a', 'd'))])
print("判断是否以 '.sh','.py'结尾", [i for i in li if i.endswith(('.sh', '.py'))])


# 利用正则表达式的捕获组来进行调整字符串格式
log = "2018-05-12, 2014-08-16, 2018-06-18"

# 利用正则捕获组的位置参数进行替换：\1 \2 \3
log_r = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
print(log_r)


# 多个小字符串拼接大字符串 str.join()
ss1 = 'qsqsqdq'
ss2 = 'sqdwfsd'
print("Join 方法：", ''.join([ss1, ss2]))

'''
    对字符串进行左，右，居中对齐
    第一种：    
        使用字符串的str.ljust(), str.rjust(), str.center()
        传入两个参数，第一个是字符串的最终长度，第二个是填充字符
    第二种：
        使用format()方法，两个参数，第一个是需要操作的字符串，第二个是格式：
        左对齐："<10" 右对齐：">10" 居中对齐："^10"
'''

'''
    去除字符串中不需要的字符的四种方法：
    第一种：   
        字符串strip(), lstrip(), rstrip()方法去掉字符串两端字符
    第二种：
        删除单个固定位置的字符，可以使用切片+拼接的方式
    第三种：
        字符串的replace()方法或者正则re.sub()删除任意位置字符
    第四种：
        字符串的translate()方法 删除多种不同字符
'''

# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表

str = "this is string example....wow!!!"
print(str.translate(trantab))