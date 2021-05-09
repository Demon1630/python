import  tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()   #创建实例

        self.main_window.title('小小胡')    #添加标题

        self.main_window.geometry('500x300')      #修改窗口大小

        #添加标签
        #bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
        l = tkinter.Label(self.main_window,text='老婆子爱你哦！',bg = 'red',font = ('Arial',12),width = 30 ,height = 2)

        #放置标签
        # Label内容content区域放置位置，自动调节尺寸
        # 放置lable的方法有：1）l.pack(); 2)l.place();
        #
        #可以在pack中添加side参数，包含 top、bottom、left、right
        # l.pack(side= 'top')
        l.pack()



        self.main_window.mainloop()               #添加循环不断刷新


my_gui = MyGUI()
