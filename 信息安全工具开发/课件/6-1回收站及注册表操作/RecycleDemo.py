
import os.path
#1.寻找当前操作系统回收站的路径
def returnDir():
    dirs = ['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):#调用os模块的函数，判断路径是否存在
            return recycleDir
    return None
#print (returnDir())

#2.遍历回收站路径，打印被删除的文件列表
path = returnDir()
def bianLi(rootDir):
    for root,dirs,files in os.walk(rootDir):# os.walk获取目录中的信息
        for file in files:#循环打印文件列表
            print (os.path.join(root,file))
        for dir in dirs:#递归调用，遍历子目录
            bianLi(dir)
#bianLi(path)

#3.用winreg模型操作注册表
import winreg
test = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\CLASSES')
key = winreg.EnumKey(test,51)
#print (key)

#4.打印不同用户（通过注册表来获取当前系统的用户信息）删除的文件列表
def bianLi(rootDir,user,sid,sys = None):
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            print (os.path.join(root,file).replace(sid,user))
        for dir in dirs:
            bianLi(dir,user,sid)
def sid2user(sid):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\"+sid)
        (value,type) = winreg.QueryValueEx(key,'ProfileImagePath')#拿到注册表ProfileList下的ProfileImagePath对应的值
        print (value)
        user = value.split('\\')[-1]#对value进行切分，用‘\’切分，-1表示切分后的最后一个值
        return user
    except:
        print (sid)
def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)#列出当前目录下所有的子目录
    print (dirList)
    for sid in dirList:#对每个目录进行操作
        files = os.path.join(recycleDir,sid)
        print (files)
        user = sid2user(sid)#将sid转换为User名
        print ('\n[*] Listing Files For User !' + str(user))
        bianLi(files,user,sid)#遍历打印删除的文件目录
findRecycled(returnDir()+'\\')