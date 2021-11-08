#前馈神经网络：
#一层神经网络由一层变为三层（input output以及隐藏层）
#输入[2,3]得到我们需要的结果
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
class Shenjing:
    def __init__(self,weight,b):#b基础偏移量
        self.weight = weight
        self.b = b;
    def amount1(self,x):#调用amount1函数实现第一步的计算
        total = sigmoid(np.dot(self.weight,x) + self.b)
        return total
    def amount2(self,h):#调用amount2函数实现第二步的计算
        total = sigmoid(np.dot(self.weight,h) + self.b)
        return total
weight = np.array([0,1])
x = np.array([2,3])
b = 0 #偏移量
a = Shenjing(weight, b)
temp = a.amount1(x)
c = np.array([temp,temp])
d = a.amount2(c)
print(d)































