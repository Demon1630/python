import  cellphone

def main():

    man = input('输入手机厂商:')
    mod = input('输入手机型号:')
    retail = input('输入手机价格:')

    phone = cellphone.Cellphone(man,mod,retail)
    print(phone)

if __name__ == '__main__':
    main()