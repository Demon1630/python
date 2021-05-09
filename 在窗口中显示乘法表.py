import tkinter
# import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('750x350')
        self.main_window.title('小小胡的乘法表')

        #禁止更改窗口大小
        self.main_window.resizable(False,False)

        # self.main_label = tkinter.Label(self.main_window,text = '***')
        # self.main_label.pack()

        #采用两个循环来使用label标签显示出来
        j = 1
        while j <= 9:
            i = 1
            while i <= j:
                self.show_label = tkinter.Label(self.main_window,text = f'{i}x{j}={j*i}',width = 30 ,height = 2)
                self.show_label.place(x=15 + i * 70, y=20 + j * 30, width=50, height=20)
                i += 1
            j += 1

        tkinter.mainloop()   #必须放在最后

my_gui = MyGUI()
