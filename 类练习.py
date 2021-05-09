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


#定义主函数，对类进行调用

def main():
    #使用硬币类创建一个对象
    my_coin = Coin()

    #显示初始时硬币初始化后的状态
    print('当前硬币朝上的一面是',my_coin.get_side())


    for i in range(10):   #投掷十次
    #投掷一次硬币
        my_coin.toss()

        # 显示投掷后硬币的状态


         #强制硬币朝上一面是正面
        my_coin.__side = 'Heads'

        # 使用 __side 可以将side这个属性设置为私有，从而在类外面无法调用更改


        # print('投掷后硬币朝上的一面是',my_coin.get_side())

        print(f'第{i+1}次投掷后，朝上一面是{my_coin.get_side()}')  #使用 f 格式输出




#调用main函数
main()


