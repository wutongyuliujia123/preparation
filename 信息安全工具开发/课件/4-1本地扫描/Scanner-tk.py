import os
import threading
import tkinter
from tkinter import messagebox
#垃圾文件后缀名
rubbishExt = ['.tmp','.bak','.old']
class Window:
    def __init__(self):#self类似于Java中的this
        #创建窗体
        self.root = tkinter.Tk()
        #创建菜单
        menu = tkinter.Menu(self.root)
        #创建system的子菜单
        submenu = tkinter.Menu(menu,tearoff=0)
        submenu.add_command(label="关于", command=self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label="退出",command=self.MenuExit)
        menu.add_cascade(label="系统",menu=submenu)
        #创建扫描子菜单
        submenu = tkinter.Menu(menu,tearoff=0)
        submenu.add_command(label="文件扫描",command=self.MenuScanRubbish)
        submenu.add_separator()
        submenu.add_command(label="文件删除",command=self.MenuDelRubbish)
        menu.add_cascade(label="垃圾扫描",menu=submenu)
        self.root.config(menu=menu)

        #创建文本框，用于显示文件列表
        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10,y=10,width=480,height=350)
        #为文本框增加垂直滚动条
        self.vscroll = tkinter.Scrollbar(self.root)
        self.vscroll.pack(side='right',fill='y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview
    def MenuAbout(self):
        messagebox.showinfo('这是扫描软件','欢迎使用本软件 \n 更多帮助请联系*****')
    def MenuExit(self):
        self.root.quit()
    def MenuScanRubbish(self):
        #设置要扫描的目录，自己实验是，填写自己的文件路径
        self.drives = ['E:/pythonProject/scannerDemo']
        #多线程的形式调用扫描函数，
        t = threading.Thread(target=self.ScanRubbish,args=(self.drives,))
        t.start()
    def ScanRubbish(self,scanpath):
        global rubbishExt#将rubbishExt设置为全局变量
        total = 0#记录扫描到的文件的数量
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        #拿到文件路径后，要获取文件的后缀名，与垃圾文件后缀名进行比对，进而判断文件是否是垃圾文件
                        filsplit = os.path.splitext(fil)
                        if filsplit[1] == '':#后缀名为空，中断本次循环，继续进行下次循环
                            continue
                        try:#判断rubbishExt是否包含filsplit[1]（文件后缀名）
                            if rubbishExt.index(filsplit[1]) >= 0:
                                fname = os.path.join(os.path.abspath(root),fil)
                                #将垃圾文件路径，写入文本框，tkinter.END是获取文本框最后的位置，从此位置开始插入
                                self.flist.insert(tkinter.END,fname + '\n')
                                total += 1
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass

    def MenuDelRubbish(self):
        # 设置要扫描的目录，自己实验是，填写自己的文件路径
        self.drives = ['E:/pythonProject/scannerDemo']
        #调用s删除函数
        t = threading.Thread(target=self.DelRubbish,args=(self.drives,))
        t.start()

    def DelRubbish(self, scanpath):
        global rubbishExt  # 将rubbishExt设置为全局变量
        total = 0  # 记录扫描到的文件的数量
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        # 拿到文件路径后，要获取文件的后缀名，与垃圾文件后缀名进行比对，进而判断文件是否是垃圾文件
                        filsplit = os.path.splitext(fil)
                        if filsplit[1] == '':#后缀名为空，中断本次循环，继续进行下次循环
                            continue
                        try:  # 判断rubbishExt是否包含filsplit[1]（文件后缀名）
                            if rubbishExt.index(filsplit[1]) >= 0:
                                fname = os.path.join(os.path.abspath(root), fil)
                                os.remove(fname)#调用删除函数，删除文件
                                #self.flist.insert(tkinter.END, fname + '\n')
                                total += 1
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
    def MainLoop(self):
        self.root.title("文件扫描器")
        self.root.minsize(500,400)
        self.root.maxsize(500,400)
        self.root.mainloop()
if __name__ =="__main__":
    windows = Window()
    windows.MainLoop()

