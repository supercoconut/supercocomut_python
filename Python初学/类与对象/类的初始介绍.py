#一个类如果没有写明继承，默认继承object类
class Student:
    pass
stu = Student()
print(dir(stu))     #dir() 是一个库函数，用于获取对象的所有属性和方法的列表
                    #但是这时我们还没有对Student()类进行定义，所以，其必然继承了其他的方法

# __str__()方法，用于返回一个对象的描述
#在我们自定义一个类之后，使用print打印这个类显示出来的信息都是对象所属类的名称以及对象所在的地址，用处不是很大
#这里就有了__str__ 与 __repr__方法这两种，当我们打印或查看某个对象时，最终看到的结果是这两个方法的返回值。这两个方法返回的都是字符串
print(stu)  #输出了内存地址
print(Student)
    #这里输出的结果都不是我们想得到的结果

#但是我们可以通过重写 __str__()方法来重新使用
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):  #而且在pycharam编译器的右侧，显示出了这个是一个重写
        return "My name is {0},my age is {1}".format(self.name,self.age)

stu = Student("zhangsan",3)
print(stu)  #这里因为上面重新写了__str__这个方法，在使用print函数后面就是调用上面定义的函数
