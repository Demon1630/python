"""
计算三个数平均值
1. 导入 tkinter 模块
2. 创建类
    2.1 创建两个 frame
    2.2创建5个标签和3个输入框
    2.3 第二个frame 中放入标签和显示标签
"""

import tkinter

class MyGUI:
    def __init__(self):

        #创建基本窗格
        self.main_window = tkinter.Tk()
        self.main_window.title('计算平均值')
        self.main_window.geometry('250x200')

        #创建上中下三个frame
        self.top_frame1 = tkinter.Frame(self.main_window)
        self.top_frame2 = tkinter.Frame(self.main_window)
        self.top_frame3 = tkinter.Frame(self.main_window)

        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #创建上frame中三个标签
        self.top_label1 = tkinter.Label(self.top_frame1,text = '数字1：',bg = 'green',width = 10,height = 1)
        self.top_label2 = tkinter.Label(self.top_frame2,text = '数字2：',bg = 'green',width = 10,height = 1)
        self.top_label3 = tkinter.Label(self.top_frame3,text = '数字3：',bg = 'green',width = 10,height = 1)

        #创建上frame 中三个输入窗口
        self.input_window1 = tkinter.Entry(self.top_frame1,width = 10)
        self.input_window2 = tkinter.Entry(self.top_frame2,width = 10)
        self.input_window3 = tkinter.Entry(self.top_frame3,width = 10)

        #使用StringVar函数创建一个接受计算结果的变量
        self.average_calcu = tkinter.StringVar()

        #创建中frame中两个显示标签
        self.mid_label = tkinter.Label(self.mid_frame,text = '三个数平均值为：',width = 20,height = 1)
        self.output_label = tkinter.Label(self.mid_frame,textvariable = self.average_calcu)   #self.average_calcu 是后面计算平均值的变量

        #创建计算按钮和退出按钮
        self.calcu_button = tkinter.Button(self.bottom_frame,text = '计算',command = self.calculate_avg,width = 10)
        self.quit_button = tkinter.Button(self.bottom_frame,text = '退出', command = self.main_window.destroy,width = 10)


        #放置frame
        self.top_frame1.pack(side = 'top')
        self.top_frame2.pack(side = 'top')
        self.top_frame3.pack(side = 'top')
        self.mid_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')


        #放置5个标签 与输入窗口
        self.top_label1.pack(side = 'left')
        self.input_window1.pack(side = 'left')

        self.top_label2.pack(side = 'left')
        self.input_window2.pack(side='left')

        self.top_label3.pack(side = 'left')
        self.input_window3.pack(side='left')

        self.mid_label.pack(side = 'left')
        self.output_label.pack(side = 'left')

        #放置按钮
        self.calcu_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')


        tkinter.mainloop()


    #定义计算按钮
    def calculate_avg(self):

        #定义三个变量来接受三个输入量
        self.num1 = float(self.input_window1.get())
        self.num2 = float(self.input_window2.get())
        self.num3 = float(self.input_window3.get())

        self.average_calcu.set((self.num1+self.num2+self.num3)/3)



my_gui = MyGUI()



