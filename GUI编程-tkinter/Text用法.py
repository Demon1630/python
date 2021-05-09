from tkinter import *

root = Tk()
text = Text(root,width=20,height=15)
text.pack()
text.insert(INSERT,"Python3 \n") #INSERT索引表示插入光标当前的位置
text.insert(END,"python算法")
mainloop()