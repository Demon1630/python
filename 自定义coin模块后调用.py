import coin

def main():
    #使用硬币类创建一个对象
    my_coin = coin.Coin()   #使用模块coin中的 Coin类 来定义对象 my_coin

    #显示初始时硬币初始化后的状态
    print('当前硬币朝上的一面是',my_coin.get_side())


    for i in range(10):   #投掷十次
    #投掷一次硬币
        my_coin.toss()

        # 显示投掷后硬币的状态

        #
        #  #强制硬币朝上一面是正面
        # my_coin.__side = 'Heads'

        # 使用 __side 可以将side这个属性设置为私有，从而在类外面无法调用更改

        # print('投掷后硬币朝上的一面是',my_coin.get_side())

        print(f'第{i+1}次投掷后，朝上一面是{my_coin.get_side()}')  #使用 f 格式输出




#调用main函数
main()

