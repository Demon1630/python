"""
使用列表存储类对象
"""

#导入手机信息模块
import  cellphone

#定义创建列表函数
def make_list():
    #创建一个空列表
    phone_list = []

    #输入手机信息
    for count in range(1,6):
        print(f'phone number {count}:')
        man = input('手机厂商：')
        mod = input('手机型号：')
        retail = input('手机价格：')

        #创建手机类
        phone = cellphone.Cellphone(man,mod,retail)

        #把创建的类添加到列表中,使用append函数
        phone_list.append(phone)

    #把列表返回出去
    return phone_list

#定义显示手机列表中所有手机信息
def dis_play(phone_list):
    for items in  phone_list:
        print(items)
        print('*'*10)

#定义主函数
def main():

    #调用列表函数创建手机列表
    phones = make_list()

    #显示手机列表信息
    dis_play(phones)

if __name__ == '__main__':
    main()