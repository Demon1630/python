"""
将摄氏度转换为开尔文
"""

import tkinter
import tkinter.messagebox

#创建类
class Temperature_gui:
    def __init__(self):

        #创建主窗口
        self.main_window = tkinter.Tk()

        #修改标题
        self.main_window.title('摄氏度转开尔文')
        self.main_window.geometry('300x300')

        #创建两个frame模块
        self.top_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #定义提示输入标签
        self.show_label = tkinter.Label(self.top_frame,text = '输入温度(℃)',bg = 'green',font = ('Arial',12),width = 10 ,height = 1)

        #定义输入窗格
        self.input_window = tkinter.Entry(self.top_frame,width = 10)

        #定义按钮
        self.calc_button = tkinter.Button(self.button_frame,text = 'Convert',command = self.calculate,width = 10)
        self.quit_button = tkinter.Button(self.button_frame,text = 'quit',command = self.main_window.destroy,width = 10,bg= 'red')


        #放置按钮
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        #放置输入窗格与提示标签
        self.show_label.pack(side = 'left')
        self.input_window.pack(side = 'right')

        #放置frame
        self.top_frame.pack(side = 'top')
        self.button_frame.pack(side = 'bottom')

        tkinter.mainloop()

        #定义转换函数
    def calculate(self):
        t = float(self.input_window.get())
        T = t + 273.15

        tkinter.messagebox.showinfo('Response', f'{t}摄氏度是{T}开尔文')  # 显示信息 surprise


temperature_gui = Temperature_gui()
