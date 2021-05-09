"""
创建一个手机信息模块
"""

#定义 手机信息类

class Cellphone:

    #初始化过程
    def __init__(self,manufact,model,retail_price):
        # 将输入的 manufact,model,retail_price 三个变量赋值给 对应类属性
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = retail_price

    #设置制造商set_manufact的方法
    def set_manufact(self,new_manufact):
        self.__manufact = new_manufact

    #设置制造商set_model的方法
    def set_model(self,new_model):
        self.__model = new_model

    #设置制造商set_retail_price的方法
    def set_retail_price(self,new_retail_price):
        self.__retail_price = new_retail_price

    def __str__(self):   #return 中换行   '\n'
        return '手机制作商为：'+ self.__manufact  + '\n' +'手机型号为：' + self.__model  +'\n'+ '手机价格为：' + self.__retail_price