# 1. 进入后显示界面

#定义显示功能界面函数
def print_info():
    print('-'*20)
    print('欢迎登入学员管理系统')
    print('1：添加学员')
    print('2：删除学员')
    print('3：修改学员信息')
    print('4：查询学员信息')
    print('5：显示所有学员信息')
    print('6：退出系统')
    print('-'*20)

info=[]   #定义空列表，存放学员信息

#定义1.添加学员函数
def add_info():


    while True:    #采用while True 循环，加上break ，可以实现在学号存在时，重新进入输入学号流程，而不是直接推出添加学员信息函数    ----还应该添加进入主界面选择
        print('请输入学员信息')
        new_id = input('学号：')


        #添加判断学号是否存在的流程，学号不能重复
        global info
        for i in info:
            if i['id'] == new_id:
                print('学号已存在，请重新输入')
                # return          #推出当前函数，但本来应该重新进入输入学号步骤
                break     #退出for 循环
        else:
            new_name = input('姓名：')
            new_tel = input('电话号码：')

            info_dict = {}             #定义空字典，存放单个学员信息
            info_dict['id'] = new_id
            info_dict['name'] = new_name
            info_dict['tel'] = new_tel

            info.append(info_dict)  #将字典添加到列表中

            print(info)
            break  #退出while True 循环

#定义2.删除学员信息函数
def del_info():

    global info

    while True:
        del_id = input('请输入删除学员学号：')
        for i in info:
            if i['id'] == del_id:
                info.remove(i)
                print(info)
                return
        else:
            print('学号不存在，请重新输入')


#定义3.修改学员信息函数
def change_info():
    global info

    while True:  #学号输入错误时循环
        change_id = input('请输入需修改学号：')
        for i in info:
            if i['id'] == change_id:
                print('请选择修改姓名或电话号码：')

                while True:  #操作输入错误时循环
                    print('1:修改姓名')
                    print('2:修改电话号码')
                    print('3:退出')
                    change_num = int(input('请输入1-2操作指令：'))
                    if change_num == 1:
                        new_name = input('新姓名：')
                        i['name'] = new_name
                        print('修改完成，学号：',i['id'],'对应新姓名为:',new_name)
                        print(info)
                        return
                    elif change_num == 2:
                        new_tel = input('新电话号码：')
                        i['tel'] = new_tel
                        print('修改完成，学号：', i['id'], '对应新电话号码为:', new_tel)
                        print(info)
                        return
                    elif change_num == 3:
                        return
                    else:
                        print('指令输入错误')
        else:
            print('学号不存在，请重新输入')


#定义4.查询学员信息函数
def find_info():

    global info
    while True:
        print('请选择查询方式：')
        print('1:利用学号查询')
        print('2:利用姓名查询')
        print('3:利用电话号码查询')
        print('4：退出')
        find_num = int(input('输入查询方式：'))
        if find_num == 1:
            while True:
                find_id = input('请输入查询学号：')
                for i in info:
                    if i['id'] == find_id:
                        for key ,value in i.items():
                            print(f'{key}:{value}')
                        return
                else:
                    print('所查询学号不存在，请重新输入')

        elif find_num == 2:
            while True:
                find_name = input('请输入查询姓名：')
                for i in info:
                    if i['name'] == find_name:
                        for key ,value in i.items():
                            print(f'{key}:{value}')
                        return
                else:
                    print('所查询姓名不存在，请重新输入')

        elif find_num == 3:
            while True:
                find_tel = input('请输入查询电话号码：')
                for i in info:
                    if i['tel'] == find_tel:
                        for key ,value in i.items():
                            print(f'{key}:{value}')
                        return
                else:
                    print('所查询学号不存在，请重新输入')

        elif find_num == 4:
            return

        else:
            print('操作输入错误，请重新输入')


#定义5.显示所有学员信息
def show_info():
    print('所有学员信息如下：')
    global  info
    print('学号\t姓名\t电话\t')
    for i in info:

        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}\t')
        # for key,value in i.items():
        #     print(f'{key}:{value}',end='\t\t')
        print()
    else:
        return




#主程序，调用所有函数
while True:   #使用while True 循环，实现每次都执行，除非输入6

    print_info()

    user_num = int(input('请输入1-6操作指令：'))  #输入的都是字符串格式，转换为整型或者浮点型，后面需跟数字进行比较

    if user_num == 1:
        # print('添加学员')
        add_info()

    elif user_num == 2:
        # print('删除学员')
        del_info()

    elif user_num == 3:
        # print('修改学员信息')
        change_info()

    elif user_num == 4:
        # print('查询学员信息')
        find_info()

    elif user_num == 5:
        # print('显示所以学员信息')
        show_info()

    elif user_num == 6:
        break

    else :
        print('输入错误')