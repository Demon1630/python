"""
使用列表接受员工信息，并显示出来
"""

import employee

#定义员工数据输入函数
def make_list():

    employee_list = []



    for i in range(1,3):

        print(f'员工{i}个人信息')
        name = input('请输入员工名：')
        ID = input('请输入员工ID：')
        department = input('请输入员工部门：')
        position = input('请输入员工职位：')

        employee_info = employee.Employee(name,ID,department,position)
        employee_list.append(employee_info)

    return employee_list

#定义信息显示函数
def show_info(employee_list):

    print('目前员工信息如下：')
    print(f'name\tID\tdepartment\tposition\t')
    for info in employee_list:

        for key,value in info.get_info().items():
            # print(f'{key}={value}')
            print(f'{value}',end='\t\t')
        print()
        # print(info)


#定义主函数
def main():

    employee_list = make_list()
    show_info(employee_list)

if __name__ == '__main__':
    main()



