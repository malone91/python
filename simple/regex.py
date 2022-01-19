import datetime
import os
import random
import re
import time

pattern = re.compile('a')
# None
print(pattern.match('n'))
# <re.Match object; span=(0, 1), match='a'>
print(pattern.match('a'))

re_compile = re.compile('ca*')

print(re_compile.match('catttt'))

# .
point = re.compile('....')
print(point.match('uaff'))

# ^ 开头 $以什么结尾   jpg$  jpg结尾 * 0次或多次

#  ca{4}t   ca{4,6}t    c[bcd]t
#  caaaat    caaaaaat      cbt,cdt,cct    .*?不适用贪婪模式,比如<a><a/> 获取一个标签

# 2018-09-12
# ....-..-..   r'\d-\d-\d'   不对换行符进行转义  ()分组   +多次

p = re.compile(r'(\d+)-(\d+)-(\d+)')
# 2018
print(p.match('2018-02-09').group(1))
print(p.match('2018-02-09').groups())
year, month, day = p.match('2018-02-09').groups()
print(year, month, day)


print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

print(datetime.datetime.now())
newtime = datetime.timedelta(minutes=10)
# 10min后时间 2022-01-15 17:59:58.058055
print(newtime + datetime.datetime.now())

oneday = datetime.datetime(2005, 5, 27)
# 2005-06-06 00:00:00
print(datetime.timedelta(days=10) + oneday)

print(random.randint(1, 5))
print(random.choice(['aa', 'bb', 'cc']))

print(os.path.abspath(''))
print(os.path.exists('ss'))