#列表——可以支持将不同数据类型的变量放在一起
#在列表中的第一个元素的位置是0，不是1！！！！！！！！(毕竟计算机是二进制)
"""
#first:
 #普通列表
member = ["a","b","c","d"]
 #混合列表
mix = [1,"e",'f',[1,2]]
 #空列表
empty = []

#second:访问列表元素:
 #从列表中获取元素:
print(member[0])    #调用第一个元素
 #访问列表的最后一个元素:
print(member[-1].title())   #因为列表的最后一个元素正好是字符串，所以可以用字符串的改变大小写等操作
 #这种负数的调用方式不仅可以用于最后一个元素，对于不知道列表长度的情况很实用
print(member[-2])   #调用倒数第二个元素
print(member[-3])   #调用倒数第三个元素，以此类推

#third:修改 增加 删除列表元素
 #修改:
member[0] = member[1]
print(member)
member[1] = "a"
print(member)   #可以直接改变列表中元素的值

 #增加元素:
 #末尾添加append(),升级版末尾添加extend(),插入insert()
 #append()一次只能添加一个元素，不能添加两个元素
member.append("葫芦娃")    #在列表最后一个元素后自动添加
print(member,len(member))
 #extend()可以往列表同时添加多个元素,其参数应该是列表！！！
member.extend(["h","i"])
print(member,len(member))
 #append()与extend()都是自动添加到列表的末位，故引入第三种方法insert()
 #insert() 两个参数 第一个是插入列表的位置，第二个数插入单个的元素或者是一个列表
member.insert(0,["h","i"])
print(member,len(member))
 #PS:这里+运算也可以实现列表的扩充

 #删除:
 #remove(),pop(),del()
 #remove()不需要知道元素在列表中的位置，知道这个元素在列表中就可以删除(不可删除不在列表中的元素)
member.remove("a")

 #del:注意del是一个语句而不是一个函数，没有括号。使用del语句需要提前知道元素在列表中的标号才可以直接删除
del member[0]
print(member)
 #del member 使用del语句也可以直接删掉列表

 #pop()将元素删掉之后，但仍然能接着使用它(被删除元素的位置也是任意的)
motorbike = ["a","b","c"]
a = motorbike.pop() #将最后一个元素删除，并且赋值给a
print(a)
 #在括号中加上位置信息,就可以让列表中任意位置的元素弹出(pop即为弹出)
motorbike = ["a","b","c"]
a = motorbike.pop(0)
print(a)

#forth:对列表进行排序(列表因为是不同类型的变量，这里简单的认为是字符串类型的列表)
 #sort()永久性排序与sorted()临时性排序
member = ["acd","bsdo","Cee","Dgr"]
member.sort()   #这让字符串改变为按字母顺序进行排序(先排大写字母)
print(member)

member = ["acd","bsdo","Cee","Dgr"]
print(sorted(member,reverse=True))  #加上reverse=True，就说明要逆着字母顺序来排序(依然是大写在前)
print(member)

member = ["acd","bsdo","Cee","Dgr"]
member.reverse()
print(member)   #同样逆着顺序，永久性的变化

#fifth 列表切片(slice) 一次性获得列表中的多个元素
 #相当于对原列表的复制，原列表不发生改变，所设定的区间是包含左侧不包含右侧
member = ["a","b","c","d"]
print(member[0:3])  #与range()函数类似，复制列表中前三个元素，不包括第四个
 #省略写法 可以忽略开始与结尾
print(member[:3])
print(member[1:])
print(member[:])    #相当于复制了整个列表
 #可以使用负数索引
print(member[-3:])  #从倒数第三个数据开始到结束
#print(member[-4,2])不可以有这种写法 要么用负数，要么用正数索引

#sixth 列表直接赋值与变量直接赋值的不同！！！！！！！！！！！！
member = ["a","b","c","d"]
member2 = member
member3 = member[:]     #将member复制到member3中，两者改变互不影响
member.append([1,2])
print(member)
print(member2)
print(member3)
                #这里改变两者中任意一个的值，另一个的值也会发生变化
                #这种情况下，member和member2是一样的，他们指向同一片内存，member2不过是member的别名，是引用。
                #member3是相当于重新创建了个列表
 #关于列表的补充:
 #相当于是重新指定一个标签
list1 = [1,2,3,4,5]
list2 = list1
list2 = [6]
print(list1,list2) #这里两个列表不同，list1与list2都是列表的标签，前一个例子member.append([1,2])相当于是列表本身直接变化(变化的不是标签)
                   #现在这个是让这个标签指向了另外一个列表，结果必然与之前不同
a = 2
b = 2
a += 1
print(str(a))
print(str(b))
                #a与b是相互独立的部分，改变其中一个的值不会影响另一个变量的值

#seventh 列表可以通过 + 来实现列表的变化
 #但是与使用上面写的三种方法不一样 个人感觉这个 + 是要对同类型的list[int]与list[str]有不一样
a = [1,2,3]
a.append("a")
print(a)
a = [1,2,3] + ["a"] #直接使用 + 会有一个高亮提示，用append可以解决这个问题
print(a)

# eighth 判断一个列表是不是空列表之后，再遍历列表：
a = []
if a:   #在条件判断时，空列表会转化成False
    for b in a:
        print(b)
else:
    print("这是个空列表")
"""

#copy()函数与deepcopy()函数  浅拷贝与深拷贝
 #copy()函数的使用方法与sort()函数是一样的
 #浅拷贝只是拷贝第一层
import copy

a = [1,2,3,4]
b = a.copy()
a.append("a")
print(a,b)  #这里a,b是两个不同的部分
a = [1,2,[3,4]]
b = a.copy()    #这里的列表中的列表[3,4]发生改变后，使用copy的部分也发生了改变
c = copy.deepcopy(a)    #深拷贝相当于是形成了一个完全与之前没有关系的部分
a[2].append(1)
print(a,b,c)
#DOI:https://blog.csdn.net/weixin_40807247/article/details/82250553?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-3.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-3.control
#clear函数，将一个列表转化成空列表
#a.clear()
#print(a,b)
#tenth 列表递推式    [ expression for item in list if conditional ]
list1 = [ i*i for i in range(10) ]
print(list1)
list2 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(list2)


