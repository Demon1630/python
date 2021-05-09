#导入tkinter库
import tkinter

#创建窗口类
class MyGUI:

    #定义初始窗口创建方法
    def __init__(self):
        self.main_window =tkinter.Tk()

        self.main_window.title('小小胡')  # 添加标题

        self.main_window.geometry('300x300')  # 修改窗口大小

        #创建main_window中创建Frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #在top_frame中创建三个标签，垂直排列
        self.main_window.label1 = tkinter.Label(self.top_frame,text='老婆子',bg = 'red',font = ('Arial',12),width = 30 ,height = 2)
        self.main_window.label2 = tkinter.Label(self.top_frame,text='我',bg = 'red',font = ('Arial',12),width = 30 ,height = 2)
        self.main_window.label3 = tkinter.Label(self.top_frame,text='爱你',bg = 'red',font = ('Arial',12),width = 30 ,height = 2)
        #放置位置为垂直
        self.main_window.label1.pack(side = 'top')
        self.main_window.label2.pack(side = 'top')
        self.main_window.label3.pack(side = 'top')


        #在bottom_frame 中创建三个标签，水平排列
        self.main_window.label4 = tkinter.Label(self.bottom_frame, text='I', bg='red', font=('Arial', 12), width=10,height=2)
        self.main_window.label5 = tkinter.Label(self.bottom_frame, text='love', bg='red', font=('Arial', 12), width=10,height=2)
        self.main_window.label6 = tkinter.Label(self.bottom_frame, text='you', bg='red', font=('Arial', 12), width=10,height=2)
        #放置位置为水平
        self.main_window.label4.pack(side = 'left')
        self.main_window.label5.pack(side = 'left')
        self.main_window.label6.pack(side = 'left')


        #放置frame
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

my_gui = MyGUI()