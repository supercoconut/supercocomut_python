#集合
 #前一个为字典，后一个为集合(没有键值对的对应)
num1 = {}
#print(type(num))
num2 = {1,2,3,4,5}
print(num2)
#print(type(num))
num2 = {1,2,3,4,5,5,3,2,1}  #集合里面的元素是唯一的，有相同的部分会自动被剔除
#print(num2[2]) 字典类型不支持索引
 #集合里的内容位置是随意的，所以不能用索引列出。可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
print(num2)
#集合的创建
 #一是直接用花括号括起来一堆数字
 #二是使用set函数 将字符串、列表、元组、range(XX)等可迭代对象转换成集合
#去除掉一个列表中的重复的元素：
set1 = [1,2,3,4,5,3,2,1,0]
temp = []
for each in set1:
    if each not in temp:
        temp.append(each)
print(temp)

print(list(set(set1)))
#一种是利用一个空列表不断的更新，一种是利用一个set函数将列表转化成集合去掉重复元素，然后再转化成列表
#第二种方法最大的问题是改变了列表的顺序！！！！！！

#增加与删减集合元素
 #使用add与remove
set2 = {1,2,3}
set2.add(6)
set2.remove(3)
print(set2)

#可以使用in与 not in判断这个元素是否在列表中
print(1 in set2)
print(4 not in set2)
#这种语句相当于一种判断，判断这个元素在不在

#不可变集合 frozenset()函数
set3 = frozenset(range(5))
print(set3)
























