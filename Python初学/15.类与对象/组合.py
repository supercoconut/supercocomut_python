#同时继承多个父类的继承与方法
#将没有继承关系的，在一个类内进行实例化
class Turtle():
    def __init__(self,x):
        self.num = x

class Fish():
    def __init__(self,x):
        self.num = x

class Fool():
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里的乌龟一共有%d只,小鱼有%d"%(self.turtle.num,self.fish.num))
    #在这个方法里面调用其他类的属性
