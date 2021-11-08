"""
import random
class Turtle():
    # 初始化
    def __init__(self, x_position, y_position, power=100, number=1):
        self.x_position = x_position
        self.y_position = y_position
        self.power = power
        self.number = number

    def move(self):
        # 能量值-1
        self.power -= 1
        new_x_position = self.x_position + random.choice([-1,-2,1,2])
        new_y_position = self.y_position + random.choice([-1, -2, 1, 2])
        #位置边界：
        if new_x_position > 10:
            new_x_position = 10 - (new_x_position - 10)
        elif new_x_position < 0:
            new_x_position = 0 - new_x_position
        else:
            new_x_position = new_x_position
        self.x_position = new_x_position

        if new_y_position > 10:
            new_y_position = 10 - (new_y_position - 10)
        elif new_y_position < 0:
            new_y_position = 0 - new_y_position
        else:
            new_y_position = new_y_position

        self.y_position = new_y_position
        return new_x_position, new_y_position

class Fish:
    def __init__(self, x_position, y_position, number=10):
        self.x_position = x_position
        self.y_position = y_position
        self.number = number

    def move(self):
        new_x_position = self.x_position + random.choice([-1, 1])
        new_y_position = self.y_position + random.choice([-1, 1])
        if new_x_position > 10:
            new_x_position = 10 - (new_x_position - 10)
        elif new_x_position < 0:
            new_x_position = 0 - new_x_position
        else:
            new_x_position = new_x_position
        self.x_position = new_x_position

        if new_y_position > 10:
            new_y_position = 10 - (new_y_position - 10)
        elif new_y_position < 0:
            new_y_position = 0 - new_y_position
        else:
            new_y_position = new_y_position
        self.y_position = new_y_position
        return new_x_position, new_y_position

#基础生成10条鱼(这里十分巧妙，把10个对象放入一个列表之中，然后再逐次调用列表)
fish = []
for temp in range(10):
    new_fish = Fish(random.randint(0,10),random.randint(0,10))
    fish.append(new_fish)

turtle = Turtle(random.randint(0,10),random.randint(0,10))
#游戏开始:
while True:

    if not len(fish):
        print("You are loser!")
        break

    if turtle.power == 0:
        print("You are loser!")
        break

    a = turtle.move()

    for each_fish in fish[:]:

        if each_fish.move() == a:   #每次进入判断，都会执行一个鱼的move函数
            turtle.power += 20
            fish.remove(each_fish)
"""
# 子类与父类(超类) 类的继承
#创建子类时，父类必须包含在当前文件夹内，并且在子类的前面
"""
class Parent:
    def hello(self):
        print("正在调用父类的方法")

#子类继承了父类的所有方法
class Child(Parent):
    def hello(self):
        print("正在调用子类的方法")

p = Parent()
p.hello()
c = Child() #子类中虽然没有任何方法，但是可以从父类中获取
c.hello()

#子类覆盖父类的方法:
#在子类中，声明一个与父类的方法同名的方法，同时父类中的方法不受影响
import random as r
class Fish():
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是：",self.x,self.y)

class GoldFish(Fish):
    pass    #pass = do nothing 保证不报错的前提下，用pass代表空语句
#子类除了继承父类，也有自身的优势
class Shark(Fish):
    def __init__(self):
        #实现调用父类的方法有两种，使用super函数即可
        super().__init__()  #super() 保留了父类没有被子类重写
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃饱了")

#多次继承
class Base1:
    def fool(self):
        print("one")

class Base2:
    def fool2(self):
        print("two")

class C(Base1,Base2):
    pass

c = C()
c.fool()
c.fool2()
"""
"""
#类、类对象与实例对象
class Show():
  count = 0

#现在有两个实例化对象
a = Show()
b = Show()
a.count += 10
print(a.count,b.count)
Show.count += 100
print(a.count,b.count)
#这里我还是用标签来说，a,b两个对象实例化之后，a.count,b.count没有经过赋值时,仍然指向Show.count
#但a.count给赋值之后，指向了10这个数据，并没有指向Show类内部的count,所以Show.count变化，对于a.count没有影响

#属性名誉方法名相同，属性会覆盖方法:
class C:
  def x(self):
    print("X-man!")

c.x = 1
#c.x() #因为上面用了一个类的属性覆盖了类中的方法，所以这里会报错


class Dog():
    def __init__(self):#这里可以有形参，作为传递的数据，也可以没有形参，自行写入
        #__init__()函数也是一种方法,根据这个类创建实例时，都会运行这一个方法
        #self相当于是让实例化的对象可以调用类中的方法与属性
        self.name = 10
        self.age = 10
#类与对象生成
#以self为前缀的变量可以供类中所有的方法使用
dog = Dog()
print(dog.age,dog.name)

#访问属性   使用句点表示法
#实例对象加属性 dog.name
#调用方法也是使用句点表示法
"""
class Capture(str):
    def __new__(cls, string):
        #__new__()方法的第一个参数是一个类
        string = string.upper()
        return str.__new__(cls,string)
a = Capture("I love Fish")
print(a)


