import os
#E:\pythonProject\scannerDemo
# def bianli(Dir):
#     for root,dirs,files in os.walk(Dir):
#         for file in files:
#             print(os.path.join(root,file))
#         for dir in dirs:
#             bianli(dir)
# Dir = 'E:\pythonProject\scannerDemo'
# bianli(Dir)
#切分文件路径，返回后缀名
fil = 'E:/pythonProject/scannerDemo/baidu.txt'
filsplit = os.path.splitext(fil)
print(filsplit)
print(filsplit[1])

