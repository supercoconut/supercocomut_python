#函数：
#def为函数的定义
"""
#username为一个形参，函数接受我在调用时，指定给username的任意值
def greet_user(username):   #声明时括号内为形参
    print("Hello!"+username.title())    #在这个地方必然username为一个字符串类型才不会出错
greet_user("Ted")   #调用时括号内为实参

#位置实参与关键字实参：
#位置实参 基于顺序
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type)
    print("My "+animal_type+"'s is"+" "+pet_name)
describe_pet("dog","Ted")   #其中dog对应着第一个形参animal_type,Ted对应着第二个形参pet_name
#关键字实参 直接赋值
describe_pet(animal_type = "dog",pet_name = "Ted")
describe_pet(pet_name = "Ted",animal_type = "dog")  #与顺序无关

#形参默认值：调用不提供参数值，即使用默认值
#def describe_pet(animal_type = "dog",pet_name):    #这种报错
def describe_pet(pet_name,animal_type = "dog"): #（语法问题）无默认值的形参要放在有默认值的形参前面
    print("\nI have a "+animal_type)
    print("My "+animal_type+"'s is"+" "+pet_name)
describe_pet(pet_name = "Ted")  #默认值
describe_pet(animal_type = "cat",pet_name = "Ted")     #不使用默认值
"""

"""
#有返回值的函数
def full_formatted_name(first_name,last_name,middle_name=" "):
    #名 中间名与姓
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
musician = full_formatted_name(first_name = "Ted",last_name = "Bob") #因为有时候没有中间名，但只输入名跟姓时还不能报错，所以给中间名一个默认的空字符，利用关键字形参来实现功能
print(musician)

def add(num1,num2):
    return num1+num2
#return 后面可以跟变量或者表达式
#return 可以返回任意类型的数据
#return 可以返回多个值（元组或者列表都是可以的）
"""

"""
#函数文档
def greet_user(username):
    print("Hello!"+username.title())
print(greet_user.__doc__)   #函数文档
# print(print.__doc__)  #将print函数的文档打印出来
"""

"""
#收集参数：
def test(*params):
    print('参数的长度是：',len(params))
    print('第二个参数为：',params[1])
test(1,'xiaojiayu',3.14,5,6,7,8)
    #收集参数相当于把输入的形参当成一个元组导入进去
    #但如果收集参数后面还需要其他参数时，要使用关键字实参或者设置成默认参数
    #当然如果把其他参数放在收集参数前面，也可以使用位置实参
def test(*params,exp):
    print('参数的长度是：',len(params))
    print('第二个参数为：',params[1])
test(1,'xiaojiayu',3.14,5,6,7,8,exp = 8)
"""
"""
#python中在函数内声明变量时，它与函数外具有相同名称的其他变量没有任何关系
def test(x):
    print("x is",str(x),sep = " ")
    x = 2
    print("Change local x to",str(x),sep = " ")
x = 50
test(x)
print("x is still",str(50),sep = " ")   #x还是50，说明在函数体中并没有改变这个值
#global可以在函数中修改全局变量
def test(a):
    print("x is",str(a),sep = " ")
    global x
    x = 2
    print("Change local x to",str(x),sep = " ")
x = 50
test(x)
print("x is still",str(50),sep = " ")
"""

"""
#内嵌函数与闭包
#内嵌函数或者是内部函数 一个函数在另一个函数里面被定义
#内部函数fun2()在外部无法被调用
def fun1():
    print("fun1()正在被调用...")
    def fun2():
        print("fun2()正在被调用...")
    fun2()
fun1()
"""
"""
#闭包
#这种函数由两个函数的嵌套组成，且称之为外函数和内函数，外函数返回值是内函数的引用
def funx(x):
    def funy(y):
        return x*y
    return funy     #这里的返回值有两种形式 一种是有括号的，一种是没有括号
                    #一个函数，如果函数名后紧跟一对括号，说明现在就要调用这个函数，如果不跟括号，只是一个函数的名字，里面存了函数所在位置的引用
#调用!!
print(funx(2)(1))

#在闭包内部函数里面不可以直接改变外部函数里面定义的局部变量的值，可以使用nonlocal表示这个变量不是局部变量空间的变量，需要向上一层变量空间找这个变量。
"""

"""
#匿名函数
g = lambda x:2*x+1  #匿名函数 后面跟的语句就是函数的返回值 是一种对于函数的精简模式
g = lambda  x,y:x+y
"""

"""#filter 过滤器
#filter[function,iterable]  其中function为函数，iterable为函数序列
    #序列中的每个元素作为参数传递给函数进行判断，返回True或者False，最后将返回True的元素放到新列表中
#function = none的情况：
a = list(filter(None,[1,0,True,False])) #list()函数将值转化成了列表形式
print(a)

#map()函数 映射函数
#map()函数将序列中的每个值作为函数的参变量进行计算，返回得到的值
a = list(map(lambda x:x*2,range(10)))   #也是两个参数 第一个参数是函数，第二个参数是序列值
print(a)
    #list()函数，以一个序列作为参数并把它转化成列表，如果参数为列表，则该参数就会被原样返回
    #使用list()函数时，程序里面不能有命名为list的变量
"""

def greet_user(username):
    """这个函数有函数文档，虽然在扯犊子"""
    print("Hello!"+username.title())
print(greet_user.__doc__)   #函数文档 其实就是现实限免的一端注释，自己不写注释就返回一个None
print(print.__doc__)   #函数文档




































