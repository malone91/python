# 人物
import re

f = open('name.txt', encoding='utf-8')
data = f.read()
print(data.split('|'))
# 武器
f2 = open('weapon.txt', encoding='utf-8')
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1


# function
def func(filename):
    print(open(filename, encoding='utf-8').read())


func('name.txt')


# 统计
def find_item(hero):
    with open('sanguo.txt', encoding='GB18030') as f:
        sentence = f.read().replace('\n', '')
        name_num = re.findall(hero, sentence)
        print('actor %s show time %s time' % (hero, len(name_num)))
    return len(name_num)


name_dict = {}
with open('name.txt', encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            num = find_item(n)
            name_dict[n] = num

name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted)