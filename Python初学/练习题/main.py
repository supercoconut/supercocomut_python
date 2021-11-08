import random
class Turtle():
    def __init__(self, x_position, y_position, power=100, number=1):
        self.x_position = x_position
        self.y_position = y_position
        self.power = power
        self.number = number

    def move(self, flag):
        self.power -= 1
        if flag == 0:  #上
            if self.y_position >= 10:
                self.y_position -= 1
            else:
                self.y_position += 1

        if flag == 1:  #下

            if self.y_position <= 0:
                self.y_position += 1
            else:
                self.y_position -= 1

        if flag == 2:  #左

            if self.x_position <= 0:
                self.x_position += 1
            else:
                self.x_position -= 1

        if flag == 3:  #右

            if  self.x_position >= 0:
                self.x_position -= 1
            else:
                self.x_position += 1

class Fish:
    def __init__(self, x_position, y_position, number=10):
        self.x_position = x_position
        self.y_position = y_position
        self.number = number

    def move(self, flag):
        if flag == 0:  # 上
            if self.y_position >= 10:
                self.y_position -= 1
            else:
                self.y_position += 1

        if flag == 1:  # 下
            if self.y_position <= 0:
                self.y_position += 1
            else:
                self.y_position -= 1

        if flag == 2:  # 左
            if self.x_position <= 0:
                self.x_position += 1
            else:
                self.x_position -= 1

        if flag == 3:  # 右
            if self.x_position >= 0:
                self.x_position -= 1
            else:
                self.x_position += 1
b = random.randint(0,9)
c = random.randint(0,9)
turtle = Turtle(b,c)
fish = Fish(b,c)
while True:
    a1 = random.randint(0,4)
    a2 = random.randint(0, 4)
    if turtle.power == 0:
        print("You are loser")
        break
    if fish.number == 0:
        print("You are winner")
        break
    if (turtle.x_position == fish.x_position) and (turtle.y_position == fish.y_position):
        turtle.power += 20
        fish.number -= 1
    turtle.move(a1)
    fish.move(a2)


