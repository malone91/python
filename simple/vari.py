from functools import reduce

# * 重复出现的次数
print('abc', end='\n\n')


def func(a, b, c):
    print('a = %s' % a)
    print('b = %s' % b)
    print('c = %s' % c)


# a = 1
# b = 2
# c = 3
func(1, c=3, b=2)


# TypeError: func() missing 1 required positional argument: 'b'
# func(1, c=3)

def howlong(first, *other):
    print(1 + len(other))


howlong(1, 3)

# var scope
var1 = 123


def f():
    var1 = 456
    # 456
    print(var1)


f()
# 123
print(var1)

# global var scope
q = 123


def f2():
    global q
    # 456
    q = 456
    print(q)


f2()
# 456
print(q)

# 迭代器 生成器
list1 = [1, 2, 3]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
# StopIteration
# print(next(it))

for i in range(10, 20, 2):
    print(i)


# for i in range(10, 20, 0.5):
# TypeError: 'float' object cannot be interpreted as an integer
# print(i)

# 生成器自己编写
def frange(start, end, step):
    x = start
    while x < end:
        yield x
        x += step


for i in frange(10, 20, 0.5):
    print(i)


# lambda
def true(): return True


lambda: True


def add(x, y):
    return x + y


print(add(3, 5))

print(lambda x, y: x + y)

# filter
arr = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x > 2, arr)))

# map
v = [1, 2, 3]
# [True, True, True]
print(list(map(lambda x: x < 4, v)))
# [2, 3, 4]
print(list(map(lambda x: x + 1, v)))

v1 = [1, 2, 3]
v2 = [3, 2, 1]
# [4, 4, 4]
print(list(map(lambda x, y: x + y, v1, v2)))

# reduce
# 7 求和 (1 + 1) + 2...
print(reduce(lambda x, y: x + y, [1, 2, 3], 1))

# zip
# (1, 4)
# (2, 5)
# (3, 6)
for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)

dicta = {'a': 'aa', 'b': 'bb'}
dictb = zip(dicta.values(), dicta.keys())
# {'aa': 'a', 'bb': 'b'}  k v反转
print(dict(dictb))


# 闭包
def f5():
    num1 = 1
    num2 = 2
    return num1 + num2

def sum(a):
    def add(b):
        # 内部函数引用外部变量称为闭包
        return a+b
    # add是函数的引用 返回内部函数的函数名称
    return add

ff = f5()
gg = sum(2)
# 6 这种写法叫闭包
print(gg(4))
# <class 'int'> 返回整数
print(type(ff))
# <class 'function'> 返回的是内部函数
print(type(gg))

# 闭包的其他案例 计数器
def counter():
    # 外部变量
    cnt = [0]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

func_ref = counter()
# 1
print(func_ref())
# 2
print(func_ref())
# 3
print(func_ref())

# 计数器从5开始
def counter_param(first = 0):
    # 外部变量
    cnt = [first]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one
func_ref5 = counter_param(5)
# 6
print(func_ref5())
# 7
print(func_ref5())
# 8
print(func_ref5())
# 9
print(func_ref5())

# 闭包更高的价值
# y = a * x + b
def a_line(a, b):
    def inner(x):
        # 内部的函数引用到了外部函数的变量
        return a*x+b
    return inner

line1 = a_line(3, 5)
# 35 只需要传入x的值  优雅一些
print(line1(10))

# Lambda的闭包写法  由传递变量改为了传递变量，参数少，代码优雅
def l_line(a, b):
    return lambda x: a * x + b

l_l = l_line(2, 3)
# 7 2*2+3 = 7
print(l_l(2))

# 函数的另一个高级功能 装饰器