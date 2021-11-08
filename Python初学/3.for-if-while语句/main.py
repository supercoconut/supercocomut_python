#基本的输入输出语句
"""
#first input() —— BIF(内置函数)
a = input()
b = input()
a = a+b
print(a)
print(type(a))
    #input() 是通过键盘的输入进行的,而且a的类型为'str'字符串,不可以直接进行加减乘除
    #type() 是显示数据类型(也是一种内置函数)
    #isinstance(a,b) 判断a与b的数据类型是否相同 返回值为True或者False
a = input("请输入你心里所想的数字:")   #这里得到的a的值跟input里面的字符串没有关系，是与输入的数值有关系

#second if-else 用缩进代表范围
if 2<3:
    print("i love you")
else:
    print("i don't love you")
    #if后面可以有很多语句，只要在缩进范围以内

#elif语句 相当于C语言中的else if(conditions)

#third while循环语法 条件为真的话执行下列语句(以缩进代表范围)
temp = input("请输入你心里所想的数字:")    #temp赋值的结果为input输入的结果，与前面的字符串无关
guess = int(temp)   #强制类型转换
while guess != 8:
    print("你猜对了")
print("游戏结束")   #这里是有问题 while存在无法结束循环的情况

#forth assert(断言)
assert 4 > 3
#assert后面的条件为假时，程序自动崩溃并抛出AssertionError的错误

#fifth random模块
import random
a = random.randint(1,10)    #生成一个随机的整数值，randint(a,b)整数的范围在a到b之间
print(str(a))   #转化成字符串输出


#len()  返回对象的长度，对于字符串——返回字符串的个数，对于列表——返回列表中元素的个数

# break与continue
#continue 结束本轮循环，进行下次循环(还是要先判断循环条件是否成立，否则直接退出循环体)
"""
"""
#first for循环
 #for可以遍历整个列表，元组或者整个字符串
 #语法格式为 for XX in XX:
people_name = ["Ted","Json","Alice"]
for a in people_name:
    print(a,end=" ")
print() #借用print后面自己的end=" "实现换行的作用
for a in "asdfgg":
    print(a,end=" ")
print()
for i in "and":
    print(i,end=" ")
print()
 #也可以利用range()函数
for i in range(1,10):
    print(i,end=' ')
 #PS:个人的理解：这个for就是在一个范围里面进行循环，这个范围可以是字符串，列表或者一个数据范围

#range()函数
 #range(start,stop,step) 前两个数是开始与结束，最后一个数是步长
 #step省略不写时默认为1
 #start可以不写，默认为0
 #一点注意！！！！range()形成的数之中不包括stop那个数
range(10) #表示0~9 这10个数

#second if语句 核心是一个True或者False的判断语句
 #用and可以检测多个条件是否满足 两侧都是判断条件，就没有对于返回值的误区
 #or也类似，只要有一个条件成立即可
#常见的结构：
 #if—else if—elif-else(if 与 elif可以引入新的判断条件，只有前面的不成立才会执行后面，else后面不跟条件)
 #如果所有的条件都要判断一遍的情况，就需要大量使用if
#PS: in 即可以在for中遍历列表或者字符串，也可以用在if while的判断之中，作为一个条件
"""
#third while循环
i = 1
while i<3:
    print(i)
    i += 1

#把in对应的作为一个判断条件:
pets = ['dog','cat','cat','turtle','goldfish','rabbit']
while 'cat' in pets:
    pets.remove('cat')
print(pets) #本质上是进入了一个循环，判断这个cat在没在pets这个列表里面

#break 与 continue语句，无论是C语言还是python
#break对if-elif-else不起作用，break是要对循环for与while起作用，都是直接跳出for与while结构(对于单层而言)，直接执行循环后面的
#continue就是继续再执行语句
