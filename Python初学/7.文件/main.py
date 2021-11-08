#打开文件
#Python中读取文本文件时,python将其中所有的文本都解读成字符串，所以对于数字，要将其转化成数值(int()或float()方法)才可以使用
 #with就是以file_object代表这个文件,并且可以自动关闭这个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()   #直接调用这个read()函数是读取文件的全部内容,要注意这个文件过大的情况
    print(contents.rstrip())
 #相比于原始文件,这个打印出来的文件内容多了一个空行，是因为read()到达文件末尾会返回一个空字符串，打印出来就是一个空行
 #rstrip()可以将多出来的空行删除

file_path = 'C:\\Users\\25394\\Desktop\\pi_digits.txt'  #注意其中的转义字符
with open(file_path) as file_object:
    contents = file_object.read()   #read()是将内容转化成了字符串
    print(contents)

#逐行读取文件:
 #对文件直接进行迭代也是读取文件内容的一种,在python里确实有这种方法，而且line中是以字符类型的一行文件的内容
with open('pi_digits.txt') as file_object:
    for line in file_object:    #这里line变量的类型也是字符串,rstrip()是把文件里面的换行符给删除了,但print()函数结束也会有一个换行符
        print(line.rstrip())

#通过with形成的文件名称，只能在with内的代码块里面调用，调用readlines()来形成一个存储这文件信息的列表
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())





































