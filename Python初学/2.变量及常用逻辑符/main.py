#变量与常用的数据类型与逻辑符
#总结优先级问题：
#幂运算 > 正负号 > 算术运算符 > 关系运算符 > 逻辑运算符

#first： + - * / // %
 #关于除法部分 真除法(/) 地板除法(floor除法 //) 以及 求余(%)
 #真除法(/) 无论除数的类型是什么，结果都是浮点型
 #求余是计算一个余数
 #floor除法不考虑操作对象的类型，总会省略掉结果的小数部分，两个数都是整型则返回整型，有一个浮点型则返回浮点型(后缀.0)
print("除法部分")
print(3/2)
print(2/2)
print(3.0/2)
print(3//2)
print(3.0//2)
print(3.0//2.0)
print(3 % 2)
 #关于乘方** 这种与负号一起使用时，记得加括号，否则就涉及到运算符优先级的问题
print("乘法部分")
print(-3**2)    #幂运算的优先级高于正负号，所以先计算了幂，再计算正负号
print((-3)**2)
print(3**-2)
#second：逻辑运算符 not and or
 #这三者是有优先级的(not > and > or)，而且and与or符合短路逻辑
 #or运算符也是这种，左侧的数为真时，就直接返回左侧数值，不计算右侧值
 #not or and都可以针对字符串进行操作 字符串分有字符与无字符两种情况
print("not and or部分")
print(3 or 4)
print(0 or 4)
print(0 or 0)
print("a" or "")
print("" or " ")    #字符串里面有一个空格不算是空字符串
 #and运算符不能简单的认为是与逻辑：and两边的数都为真时，返回左侧的值。而and左侧的数为0时，就不会计算右侧的值，直接返回0 (这就是短路逻辑)
print(1 and 3)
print(0 and 3)
print("a" and "")   #若有空字符串输出空行
print("a" and "b")  #若两侧均有字符串输出右侧字符串
 #not 返回的值是True或者False
 #对于布尔值，非运算会对其进行取反操作，True变False，False变True
 #对于非布尔值，非运算会先将其转换为布尔值，然后再取反。
  #字符串，有内容转化成为True,空字符串转化成为False
  #数字，0表示为False ,其它表示为True
print(not 4)
print(not 0)
print(not "")
print(not "a")

#third 关系运算符:比较大小以及判断等于不等于关系，表达式为真返回True,表达式为假返回False
print("关系判断")
print(3 < 2)
print(2 == 2)
print(2 != 3)   # ==判断相等 != 判断不相等
#关系运算符还有<= >=等等
#而且python比较运算符与C语言不同 90 <= a <= 100(在python中可以)，C语言的写法为90 <= a && a <= 100

#forth None类型
 #表示该值是一个空对象。空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
 #在做判断时，None作为False
a = None
print(a)

#fifth bool类型
 #True=1，False=0,可以用True与False作为0 1常值参与算术运算，只是显得很傻罢了
 #同时不只是0与1可以代表True与False，其他类型在条件判断时也会被按True与False处理(比如空字符串与空列表)
 #PS:~为取反，对于这些有正负之分的数据来说，~等于先取相反数再-1，毕竟计算机的数据都是补码形式，符号位为1则为负，符号位为0则为正
print("bool类型")
a = 3
a = ~a
print(a)
a = -4
a = ~a
print(a)
a = True + False
print(str(a))

# 基本数据类型：int,float,str
 #float(),int()都可以将字符串类型的数据转化成浮点型与整型，不过这个字符串内部要全部为数字(不可以有.)!!!!
print("基本数据类型")
a = "123"
print(int(a))
print(float(int(a)))   # a = "123.5"这种情况也不行！！！！
 #其中的float类型的变量在使用%-string格式化输出，默认是6位小数，其他运算与格式化除数都是默认为1位小数，若有更多位数就取最大的位数
 #而且在python中没有double类型，只有float类型！，所以python中的float与C语言中的double类型
a = 123.5
print(int(123.5))   #小数转整数，小数点后的数直接被省略掉！！

# 成员资格运算符 in
#用于检测一个变量是否在序列之中，在序列中返回True,不在返回False




