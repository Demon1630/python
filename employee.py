"""
定义一个员工信息类 包含姓名，ID号码，部门和职位方法
"""

class Employee:
    def __init__(self,name,ID,department,position):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__position =position


    #定义设置方法
    def set_name(self,new_name):
        self.__name = new_name

    def set_ID(self,new_ID):
        self.__ID = new_ID

    def set_department(self,new_department):
        self.__department = new_department

    def set_position(self,new_position):
        self.__position = new_position

    #定义显示方法
    def get_info(self):
    # def __str__(self):

        # return  '用户名为：'+ self.__name +'用户ID为：' + self.__ID +'用户部门为：'+self.__department +'用户职位为：'+ self.__position
        return {'name':self.__name,'ID':self.__ID,'department':self.__department,'position':self.__position}
