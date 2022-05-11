#encoding=utf-8
from scapy.all import *
##1.网卡开启嗅探，并收集数据
# package = sniff(iface="Realtek PCIe GBE Family Controller",timeout = 10)
# #讲捕获的数据包存入Demo.pcap
# wrpcap('Demo1.pcap',package)

#2.用python解析数据包
# import scapy.all as scapy
# packages = scapy.rdpcap("Demo1.pcap")#加载离线的数据包,使用相对路径
# #print(packages[497].show())#解析包内容，packages类似一个数组，用数组下表的形式访问
# print(packages[497].mysummary)#第二种解析方式

#3.解析出HTTP请求的数据
import scapy.all as scapy
packages = scapy.rdpcap("E:\\pythonProject\\unit7\\Demo1.pcap")#使用绝对路径加载
for p in packages:
    for f in p.payload.payload.payload.fields_desc:
        fvalue = p.payload.payload.getfieldval(f.name)
        reprval = f.i2repr(p.payload.payload,fvalue)#转换为十进制字符串
        if 'HTTP' in reprval:
            lst = str(reprval).split(r'\r\n')
            for l in lst:
                print(l)


