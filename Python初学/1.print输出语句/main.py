#print函数的用法
#print函数的原型  print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#first
a = 1
print(a)    #对于数值型变量 直接输出值
print(5+3)  #对于数学表达式，可以直接输出表达式结果

#second
a = "hello world"
print(a)    #对于字符串变量可以直接输出
print("hello world")    #直接输出变字符串也可以

#third 一次输出多个变量
a = "hello world"
b = 1
print(a,b)  #两个输出用空格隔开
print(a,b,sep='.')  #设置间隔方式 否则默认是空格
print("Duan"+"Yixuan")   #输出DuanYixuan 中间没有空格

#fourth +与*在字符串中的使用
print("well water"+" "+"river water")    #字符串的拼接
                                        # 只有相同类型的才可以拼接 5+"fefni"会报错
                                        #但是可以对于不是字符串类型的数据进行强制类型转换 str(5)+"fefni"是可以的
first_name = "Zhang"
last_name = "Deteng"
full_name = first_name+" "+last_name
print(full_name)               #这种方式也是一种字符串的拼接
print("well water"+str(4))    #字符串的拼接 只有相同类型的才可以拼接 5+"fefni"
print("well"*3)         #字符串的重复生成
print("well\n"*3)       #与之前最大的不同是每一个字符串后都多了一个换行符

#fifth 字母大小写变换
name = "adc lovelace"
print(name.title()) #每个单词的首字母都转变成大写形式
print(name.lower()) #字符串所有的字母均转化成小写
print(name.upper()) #字符串所有的字母均转化成大写
                    # 这三种操作均不改变字符串本身的内容，只是改变输出形式

#sixth 制表符 \t 与换行符 \n (这两种只有在字符串中表示指标与换行)
#PS:关于反斜杠是有很多的应用 比如 "与' 字符串中可以有'与"(只要不相互冲突就好，字符串用”包围起来，中间可以有')，或者可以用\' \" \\来输出 ’与 “ 和 \
print("\'","\\","\"")
#制表符的写法是\t，作用是对齐表格的各列
#制表符的写法是\t,本意是取table键的意思
print("学号\t\t姓名\t语文\t数学\t英语")
print("2017001\t曹操\t99\t88\t0")
print("2017002\t周瑜\t92\t45\t93")
print("2017008\t黄盖\t77\t82\t100")


#seventh 删除输入数据中多余空白 字符串中多余的空格是有意义的,多一个空格字符串也不一样
#rstrip()确保字符串末尾没有空白
#lstrip()确保字符串开头没有空白
#strip()确保字符串两侧没有空白
#rstrip(),lstrip(),strip()也不会改变字符串本身
a = "python "
print(a.rstrip())
print(a)
a = '12345'
print(a.rstrip('45'))
 #这三个的作用不仅仅是删除掉空格这么简单,参数为空时,那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)。
 #参数里面可以是你想删除的任意字符
#eighth 数据的格式化输出与C语言类似
#DOI https://blog.csdn.net/sinat_28576553/article/details/81154912?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162607893616780357241515%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=162607893616780357241515&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-81154912.first_rank_v2_pc_rank_v29&utm_term=python++print&spm=1018.2226.3001.4187
#这里与C语言不太一致，print的格式控制符与转化说明符


#ninth print与end一起使用：
f = "fishc"
for i in f:
    print(i,end=" ")
    print(i+" ")        #print中有end=" " 会使该函数关闭在输出中自动包含换行的默认行为,而是以空格结束字符串
                        ##print(i,end="")这种形式是输出一个字符后面没有空格

#直接输出列表或者元组也可以

