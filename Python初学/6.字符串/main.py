#字符串：python中没有字符这种变量类型，只有字符串
#字符串一旦确定也不可以修改，与元组一样，也是通过创建新的字符或者替换原有字符串来得到修改的效果

"""
#firth  原始字符串
#在字符串前面加一个r或R表示其为原始字符串——原始字符串是解决字符串里面有\加字母误判为转义字符的情况  但是原始字符串的结尾不可以以"\" 结尾
#原始字符串最后为\的形式：
temp = str = r'C:\Program Files\FishC\Good'+'\\'  #或者写成str = r'C:\Program Files\FishC\Good''\\' 加号可以忽略
print(temp)

#second 字符串拓展
s = "adc"
#对于字符的判断，其中返回值都是True，False类型
s.isalnum() #字符串不为空，并且字符全部为字母或者数字，返回True
s.isalpha() #字符串不为空，并且字符全部为字母，返回True
s.isdigit() #字符串中字符全部为数字,返回True
s.isdecimal() #字符串中只包含十进制数字为True，否则为False
s.isnumeric() #字符串中只包含数字字符，返回True
s.islower() #字符串中的字母全部为小写字母，返回True
s.isupper() #字符串中的字母全部为大写字母，返回False
s.istitle() #字符串是标题化的(所有的单词均以大写开始并且其他字母均为小写)
s.isspace() #字符串中只有空格，返回True

#third 字符串的切片：
a = "I love fishC"
print(a[:6])
 #字符串的索引 与元组、列表一致
print(a[6])
 #关于字符串的更新
 #一开始 a = "I love fishC"
a = a[:4] + "but" + a[6:]
 #现在标签a指向了一个新的字符串，原来的字符串没有标签指向它。
print(a)
#fourth 变化类型:
 #将字符串的第一个字符改为大写
a = "i love fishC"
print(a.capitalize())
 #将字符串的第所有字符改为小写
a = "I Love fishC"
print(a.casefold())
 #width()字符串居中，并用空格填充至长度为width(一般左跟右都会有)
print(a.center(40))
 #count(str,start,end)
print(a.count("i",2,10)) #后面两个数代表索引
print(a.count("i"))    #不加start与end代表在整个字符串里面寻找
 #endwith(sub,start,end)    #检查字符串是否已sub子字符串结束，如果是返回True,如果不是返回False
print(a.endswith("C"))
 #expandtabs()  #将字符串中的tab(\t)转化成空格，如不是指定参数，默认的空格是tabsize = 8
a = "i \tlove fishC"
print(a.expandtabs())
 #find(sub,start,end) 寻找sub字符串是否在给定的范围里面，有则返回索引值，没有则返回-1
 #index(sub,start,end)  与find方法类似，但是如果字符不在，程序会发生异常

#字符串的格式化 format
#位置参数
print("{0} love {1}.{2}".format("I", "fishC", "com"))
#关键字参数
print("{a} love {b}.{c}".format(a="I", b="fishC", c="com"))
#位置参数与关键字参数混合 但位置参数必须在关键字参数之前 否则会报错
print("{0} love {b}.{c}".format("I", b="fishC", c="com"))

print("{b} love {c}.{0}".format("I", b="fishC", c="com"))
#print("{b} love {c}.{0}".format("I", b="fishC", c="com"))

print("{{0}}".format("a"))  #在format中 在一层花括号外加另一层花括号的意思是转义，即输出花括号本身，这样就没有了标识，就不会打印出a
print("{{{0}}}".format("a"))   #最外层的两层为转义，得到一对大括号，最中心的一对大括号翻译成字符串a，最终打印出{a}

"""
#多重字符串 可以实现多行的调用
#second 三重引号字符串+关于enter键的一点延伸使用
#""" 三个单引号或者双引号之中的为，可以实现多行书写的字符串"""
str1 = """my friend
your name is in my heart"""
print(str1)
    #friend后面按下一次enter键，相当于在字符串末尾多输入了一个\n\r(先换行，然后将光标移到下一行开始)
str1 = """my friend
your name is in my heart
"""
print(str1)
    #这个在heart的后面多了一个\n\r 所以实际的输出效果 是要多出一个空白行来
str1 = """my friend\n\ryour name is in my heart"""
print(str1)
    #结果与第一种情况类似
#"""还可以作为多行注释符来使用

"""
#third
 #join() 在字符串、列表中插入其他的字符串
a = "|"
print(a.join(["a","b","c"]))
print(a.join("ab"))
 #ljust(width) 将字符串左对齐并且用空格将长度填充到width指定长度
a = "adc"
print(a.ljust(10))
"""

print("{0:.1f}".format(123.455))























