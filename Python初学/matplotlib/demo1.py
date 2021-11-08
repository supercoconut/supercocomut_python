import matplotlib.pyplot as plt
values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.title("Squares Numbers",fontsize = 24)  #字体大小
plt.xlabel("Values",fontsize = 14)
plt.ylabel("Squares",fontsize = 14)
plt.tick_params(axis = 'both',width = 1,labelsize = 14)   #同时设置x y轴的分度值大小,width为分度值，labelsize也为字体大小
plt.plot(values,squares,linewidth = 5)  #字体宽度
plt.show()  #显示
