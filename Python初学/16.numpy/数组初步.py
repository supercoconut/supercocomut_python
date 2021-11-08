import numpy as np
#定义一个数组(Python自身仅支持低维数数组)使用numpy库可实现高维
a = np.array([2,3,4])
print(a)

#高维数组
a = np.array([(1,2),(3,4)])
print(a)

#输出数组的行数与列数
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

#在原数组的基础上调整数组行数与列数
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2)  
print(b)

#mean() 计算平均值
y_true = np.array([0,1,1,0])
y_false = np.array([1,1,1,1])
total = ((y_true - y_false)**2).mean()
print(total)

#



