#-*- coding:utf-8  -*
#1.解析IP地址，获取IP地址对应的城市信息
# import pygeoip
# #gi = pygeoip.GeoIP('GeoLiteCity-data-master/GeoLiteCity.dat')
# gi = pygeoip.GeoIP('D:\\pyws\\GeoLiteCity-data-master\\GeoLiteCity.dat')
# rec = gi.record_by_addr('15.29.148.130')
# print (rec)

#2.解析数据包，获取数据包的内容和数据
import dpkt
f = open('dpktDemo.pcap')
pcap = dpkt.pcap.Reader(f)
for i in pcap:
    print (type(i))
    print (i)