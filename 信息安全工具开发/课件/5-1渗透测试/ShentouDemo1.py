#使用循环迭代模块itertools
import itertools as its
#将字典需要的元素赋值给words变量
words = "123456789!@#$%^&*qwertyuiopasdfghjklzxcvbnm"
#假设我们的密码是4位，那么指定repeat = 4
r = its.product(words,repeat = 4)
#将生成的密码保存到文档中
with open('pass.txt','w+') as fp:
    for x in r:
        fp.write("".join(x)+"".join("\n"))