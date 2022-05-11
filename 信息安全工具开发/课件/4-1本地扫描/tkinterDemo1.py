# -!- coding: UTF-8 -!-
import tkinter
from tkinter import *
#1.GUI编程入门小实验
# window = tkinter.Tk()#创建窗体
# window.title("First Window")#设置窗体名字
# window.geometry("700x400")#设置窗口大小
# #添加标签
# label = tkinter.Label(window, text = "Hello World!",font=("Arial Bold",10))#创建标签组件，并加入到窗体里
# label.grid(column=0,row=0)#控制控件相对于父控件的位置
# #添加文本输入框
# txt = Entry(window,width=10)#width=10输入框的宽度
# txt.grid(column=1,row=0)
# txt.focus()#使程序运行后就获取焦点
# #接收按钮点击事件的函数
# def clicked():
#     res = "Welcome to " + txt.get()#获取输入框的内容
#     label.configure(text=res)
# #添加按钮，设置颜色、设置点击事件
# btn = Button(window,text='click me',bg='orange',fg = 'red',command=clicked)#按钮
# btn.grid(column=2,row=0)
# window.mainloop()

#2.组合框的使用
#2.1下拉列表
# from tkinter.ttk import Combobox
# window = Tk()
# window.title("组合框")
# window.geometry("700x400")
# combo = Combobox(window)
# combo['values'] = (1,2,3,4,5,"Text")#设置下拉列表的内容
# combo.current(3)#设置启动后下拉框显示的值
# combo.grid(column=0,row=0)
# print(combo.get())#获取当前被选中的值
# window.mainloop()

#2.2复选框

from tkinter.ttk import Combobox
# window = Tk()
# window.title("复选框")
# window.geometry("700x400")
# chk_state = BooleanVar()
# chk_state.set(False)#设置启动时状态
# chk = Checkbutton(window,text="Choose",var = chk_state)
# chk.grid(column=0,row=0)
# window.mainloop()

#2.3单选框，
# window = Tk()
# window.title("单选框")
# window.geometry("700x400")
# lal = Label(window,text="show value")
# selected = IntVar()
# def clicked():
#     #print("选项被更改")
#     lal.configure(text=selected.get())
# btn = Button(window,text="Click Me",command=clicked)#点击，运行clicked()方法
# rad1 = Radiobutton(window,text='first',value=1,variable=selected)#创建单选按钮
# rad2 = Radiobutton(window,text='Second',value=2,variable=selected)
# rad3 = Radiobutton(window,text='thrid',value=3,variable=selected)
# rad1.grid(column=0,row=0)
# rad2.grid(column=1,row=0)
# rad3.grid(column=2,row=0)
# btn.grid(column=3,row=0)
# lal.grid(column=0,row=1)
# window.mainloop()

#2.4文本区域
# from tkinter import scrolledtext
# window = Tk()
# window.title("文本区域")
# window.geometry("700x400")
# txt = scrolledtext.ScrolledText(window,width=40,height=10)
# txt.insert(INSERT,"扫描结果为：")
# txt.grid(column=0,row=0)
# window.mainloop()
#2.5消息框
# from tkinter import messagebox
# window = Tk()
# window.title("文本区域")
# window.geometry("700x400")
# def clicked():
#     messagebox.showinfo("弹窗名","Message content")#建立消息弹窗
# btn = Button(window,text="Click here",command=clicked)
# btn.grid(column=0,row=0)
# window.mainloop()

#2.6 Spinbox控件，指定范围
window = Tk()
window.title("文本区域")
window.geometry("700x400")
#spin = Spinbox(window,from_=0,to=100,width=5)#指定范围
spin = Spinbox(window,values=(3,8,11),width=5)#指定具体的值
spin.grid(column=0,row=0)
window.mainloop()