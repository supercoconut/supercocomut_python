#编码一个神经元实现运算，使用了numpy库，只有一层，而且权重是我们自行赋值的
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
class Shenjing():
    def __init__(self,weight,b):
        self.weight = weight
        self.b = b
    def output(self,input):
        amount = np.dot(self.weight,input) + self.b
        return sigmoid(amount)

weight = np.array([0,1])
b = 10
input = np.array([2,3])
a = Shenjing(weight, b)
c = a.output(input)
print(c)