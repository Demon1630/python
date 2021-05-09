#导入模块
import tkinter
import tkinter.messagebox

#定义窗口类
class MyGUI:




    def __init__(self):
        #创建窗口实例
        self.main_window = tkinter.Tk()

        self.main_window.geometry('100x100')
        self.main_window.title('小小胡')
        b = 1

        # 定义点击按钮后操作
        #创建按钮实例
        self.my_button =tkinter.Button(self.main_window,text = '点我',command = lambda a=b: do_something(a))  #do_something 作为回调函数

        #创建退出按钮
        self.quit_button = tkinter.Button(self.main_window,text = '退出',command = self.main_window.destroy)

        #放置按钮
        self.my_button.pack(side = 'top')

        self.quit_button.pack(side = 'top')

        def do_something(a):
            if a == 1:
                tkinter.messagebox.showinfo('Response', 'surprise')  # 显示信息 surprise
            else:
                tkinter.messagebox.showinfo('Response', 'wrong')  # 显示信息 surprise

        #添加窗口循环
        tkinter.mainloop()




my_gui = MyGUI()


