#用户输入input()
"""
 #input()函数接受一个函数，即向用户显示的提示与说明
a = input("请输入一个数：")
print(type(a))
print(isinstance(a,str))
 #PS:三个BIF(内置函数)，input,type,isinstance
 #type()函数
 #isinstance(object, classinfo) object是针对的对象，classinfo是直接或间接类名、基本类型或者由它们组成的元组
  #字符串str,整型int
"""
#对于提示超过一行情况:把提示的字符保存的一个变量里面
prompt = "请轻轻地来，轻轻地去"
prompt += "\n这样我才会爱你"
prompt += "\n请输入我心中的数值："
a = input(prompt)
print(a)



