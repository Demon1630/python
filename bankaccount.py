# 定义一个银行账户模块

class Bankaccount:

    #定义一个初始账户额
    def __init__(self,bal):     #bal 为输入的初始额度
        self.__balance = bal

    #定义存钱过程
    def deposit(self,account):
        self.__balance += account

    #定义取钱过程
    def withdraw(self,account):
        # 判断账户中是否有足够的钱，够的话取出来，不够报错
        if self.__balance < account:
            print(f'目前账户只有{self.__balance},余额不足')
        else:
            self.__balance -= account

    # 定义显示当前余额过程
    def get_balance(self):
        return  self.__balance

    # 使用 __str__(self) 函数来输出 __balance  在调用时就可以直接输出  print(类)   而不是 print(类.get_balance())
    # 不需要再定义 get_balance()函数了
    def __str__(self):
        return format(self.__balance, ',.2f')


