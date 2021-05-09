#导入tkinter库

import tkinter

#创建主窗口
main_window = tkinter.Tk()
main_window.geometry('500x500')
main_window.title('计算器')
main_window.resizable(0,0)


#创建显示窗格
value_calcu = tkinter.StringVar()
shao_window = tkinter.Entry(main_window,textvariable = value_calcu)

#将显示窗格设置为只读,只用于显示
shao_window['state'] = 'readonly'

#设置放置位置
shao_window.place(x=50,y=20,width=400,height = 50)

#放置键盘按钮
bvalue = ['C', '+', '-', '//', '7', '8', '9', '√', '4', '5', '6', '*', '1', '2', '3', '/', '.', '0', '^', '=']

#将按钮按照 5*4 放置
i = 0




for row in range(5):
    for col in range(4):
        buttons = bvalue[i]
        # button_show = tkinter.Button(main_window,text = buttons,command = lambda x =buttons: onclock(x))
        button_show = tkinter.Button(main_window,text = buttons,command =lambda x=buttons:onclock(x))
        button_show.place(x = 50+col*105,y =120+row*80,width = 80,height=50 )
        i+=1

#定义运算逻辑
def onclock(buttons):

    content = value_calcu.get()
    #根据按钮做出反应
    if buttons in '0123456789+-*/^=.√//':
        #按下0-9在显示窗口中显示出来
        content += buttons
    # elif buttons == '.':
    elif buttons == 'C':
        content = ''
    elif buttons == '=':
        content += buttons

    value_calcu.set(content)










tkinter.mainloop()