# 元组 常量
import time

name = (
    u'摩羯座', u'水瓶座', u'双鱼座',
    u'白羊座', u'金牛座', u'双子座'
)
days = (
    (1, 20), (2, 19), (3, 21),
    (4, 41), (5, 21), (6, 22)
)

(month, day) = (2, 15)

myday = filter(lambda x: x <= (month, day), days)

length = len(list(myday)) % 12
print(name[length])

# 列表，可修改
list1 = ['abc', 'xyz', 'm']
print(list1)
list1.remove('xyz')
print(list1)

# 会报错
# list1.remove('a')
# print(list1)

# input
chinese = '甲乙丙丁'
# 3
index = int(input('请输入'))
if (chinese[index % 4]) == '丁':
    print('丁丁')

for i in range(1, 13):
    print(i)

num = 5
while True:
    print('a')
    time.sleep(0.1)
    num = num + 1
    if num > 10:
        break

# dict
dict1 = {}
# <class 'dict'>
print(type(dict1))
dict2 = {'x': 1, 'y': 2, 'z': 3}
print(dict2)

# 从1-10所有偶数的平方
aList = []
for i in range(1, 11):
    if i % 2 == 0:
        aList.append(i*i)
print(aList)

bList = [i*i for i in range(1, 11) if(i % 2 == 0)]
print(bList)

# file
file1 = open('name1.txt', 'w')
file1.write('欧文')
file1.close()

file2 = open('name1.txt')
print(file2.read())
file2.close()

file3 = open('name1.txt', 'a')
file3.write('哈哈')
file3.close()

file4 = open('name1.txt')
print(file4.readline())
file4.close()

file5 = open('name1.txt')
for line in file5.readlines():
    print(line)
    print('1111')

# exception
d = {'a':1, 'b': 2}
# KeyError: 'c'
try:
    print(d['c'])
except KeyError:
    print('key错误哦')

try:
    print(1/0)
except ZeroDivisionError as e:
    print('wrong %s' %e)


try:
    print(1/'a')
except Exception as e:
    print('捕获所有异常 %s' %e)

# throw exception
try:
    raise NameError('helloError')
except NameError:
    print('name error')

# try finally
try:
    a = open('name1.txt')
except Exception as e:
    print(e)
finally:
    a.close()