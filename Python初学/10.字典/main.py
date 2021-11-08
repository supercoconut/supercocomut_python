#字典类型 构成键-值对
#键与值之间用: 键值对之间用,
#值的类型是任意的，但键的类型是固定的，只能是字符串，数组或者元组
alien = {"color": 'green',"points": 5}
print(alien["color"])

#字典是动态的，可以添加与删除
 #只要指定字典名，用方括号括起来的键与相关联的值即可
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)    #这样就添加了x位置与y位置
 #一般可以先定义一个空字典，然后再添加键值对
alien_0 = {} #空字典

#字典值的修改
 #与字典中的值的添加一样，直接指定字典名，键值与其对应的新值就行
alien['x_position'] = 10
print(alien)

#删除键值对
 #使用del语句
#del alien_0 #删除整个字典
del alien['color']
print(alien)

#多行字典的表示方式
alien_1 = {
    'a':'C',
    'b':'python',
    'c':'C++',  #最后一行这里可以有也可以没有,
}
print(alien_1)
alien_1['d'] = 'java'
print(alien_1)

#遍历字典:
 #在遍历字典时，键值返回的顺序与储存顺序不同，Python不关心键值对的存储顺序，只跟踪键与值的关联关系
 #引入了items()方法
for key,value in alien.items():
    print(key,value,sep=" ",end=";")
print()
 #使用items()，就可以返回键值，前一个变量储存键，后一个变量存储值

#编历字典中的所有的键
 #使用keys()方法
 #与items()一样，直接在后面加后缀
for key in alien.keys():
    print(key,end=" ")
print()

#有顺序编历字典中的所有键：
 #采用sorted()函数
for key in sorted(alien.keys()):    #按字母顺序编历
    print(key,end=" ")
print()
#编历列表中的值
 #采用values()方法
for key in alien.values():
    print(key,end=" ")
print()

#嵌套:字典与列表之间
 #创建一个列表，其中的元素时字典
aliens = []
for alien_number in range(3):    #创建三个外星人
    new_alien = {"color": 'green', "points": 5}
    aliens.append(new_alien)    #new_alien只是一个标签，列表中存储的元素是这个标签对应的字典
print(aliens)
 #字典中包含列表
pizza = {
    'crust' : 'thick',
    'topping' : ['mushroom','extra cheese']
}
for i in pizza['topping']:
    print(i,end=" ")
print()
 #字典中包含字典: 这个就可以使用之前的items()方法来得到键值
users = {
    'alien_0':{
        'first':'a',
        'second':'b',
    },
    'alien_1':{
        'first':'a',
        'second':'b'
    },
}
for key,value in users.items():
    for key1,value1 in value.items():
        print(key1,value1)





















