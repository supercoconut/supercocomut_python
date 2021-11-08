# 特殊属性
# __dict__ 获得类对象或实例对象所绑定的所有属性与方法的字典
print(dir(object))  # dir() 用于返回对象内部的所有属性、方法名称组成的序列


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建实例对象:
x = C("jack", 20)
print(x.__dict__)  # 实例对象会输出属性
print(C.__dict__)  # 类对象会输出属性与方法

# __class__，输出实例对象所属的类对象
print(x.__class__)
print(C.__base__)  # 输出第一个父类
print(C.__bases__)  # 输出父类类型的元组

print(C.__mro__)  # 找到类对象的层次结构


# 特殊方法
# __add__(self,other)
class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("zhangsan")
stu2 = Student("lisi")
s = stu1 + stu2
print(s)  # 两个对象执行相加，需要使用__add__()方法
s = stu1.__add__(stu2)
print(s)
# __len__()
list = [11, 22, 33, 44]
print(len(list))
print(list.__len__())
print(len(stu1))  # 这里在类中不定义这个函数是会报错的


# __new__ __init__
#在一个类中 优先执行的是__new__ 然后再调用__init__
