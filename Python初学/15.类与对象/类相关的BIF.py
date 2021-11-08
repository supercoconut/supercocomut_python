#issubclass(class,classinfo) 第一个参数是不是第二个参数的之类
#这种类型是比较宽松的检查，尤其是类本身也可以是自己的之类 返回值为True或者False
class A:
    pass
class B(A):
    pass
print(issubclass(A,A))
print(issubclass(B,A))

#isinstance(object,classinfo)  classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组
#用于判断两者是不是同一种类型的变量，比type()更方便的是，isintance()会将子类判断为与其父类同种类型,也可以去判断实例化对象与类
#对象(object)的类型与参数二的类型(classinfo)相同则返回 True，否则返回 False。
#对于classinfo是元组的情况！！！！！！
a = 3
isinstance (a,(str,int,list))    # 是元组中的一个返回 True
