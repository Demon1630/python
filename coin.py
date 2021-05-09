import  random

#定义类   硬币 包含初始化过程   投掷过程   获取硬币状态过程

class Coin:

    #1.初始化过程
    def __init__(self):
        self.__side = 'Heads'

    #2.投掷过程
    def toss(self):
        #使用随机数函数获得朝上一面状态
        if random.randint(0,1) == 0:
            self.__side = 'Heads'
        else:
            self.__side = 'Tails'

    #3.获取硬币状态过程
    def get_side(self):
        return self.__side    #将硬币此时状态返回，因为是函数，所以使用return

