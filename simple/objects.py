user1 = {'name': 'tt', 'hp': 200}
user2 = {'name': 'gg', 'hp': 20}
def print_u(u):
    print('name is %s hp is %s' %(u['name'], u['hp']))

print_u(user1)
print_u(user2)


# 定义一个类 首字母大写
class Player():
    def __init__(self, name, hp): #初始化方法
        #  self.__name 不被访问到
        self.name = name
        self.hp = hp
    def print_u(self): #定义一个方法
        print('name is %s hp is %s' %(self.name, self.hp))

    def updateName(self, newName):
        self.name = newName


# 类的实例化
user3 = Player('rr', 30)
user4 = Player('aa', 20)
user3.print_u()
user4.print_u()
user4.updateName('wilson')
user4.print_u()

# 先写pass，然后慢慢定义属性
class Monster():
    def __init__(self, hp = 100): #默认值
        self.hp = hp

    def run(self):
        print('跑')

# 继承
class Animal(Monster):
    def __init__(self, hp=1):  # 默认值
        self.hp = hp

class Boss(Monster):
    pass

a1 = Monster(23)
print(a1.hp)
a1.run()
a2 = Animal(2)
print(a2.hp)
a2.run()


class AnimalN(Monster):
    def __init__(self, hp=1):  # 默认值
        super.__init__(hp)

# 子类 True
print(isinstance(a2, Monster))
# 子类属性覆盖父类


# with
class TestWith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常')
        else:
            print('异常 %s' %exc_tb)

with TestWith():
    print('running')
    raise NameError('哈哈哈')