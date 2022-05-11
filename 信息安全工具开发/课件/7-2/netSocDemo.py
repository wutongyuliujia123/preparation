#1.DNS的嗅探
# import scapy.config
# from scapy.all import *
# from scapy.layers.inet import UDP
# scapy.config.conf.sniff_promisc = True#设置混杂模式
# def packetHandler(pkt):
#     print(pkt.summary())
#     udp = pkt.getlayer(UDP)
#     print(udp.show())
# if __name__ == '__main__':
#     dev = "Realtek PCIe GBE Family Controller"
#     filter = "udp port 53"
#     sniff(filter = filter,prn = packetHandler,iface = dev)

#2.用嗅探的方式监听主机的ping
# import socket
# import os
# #监听的主机
# host = '179.16.125.216'
# #创建原始套接字，然后绑定在公开的接口上
# if os.name == 'nt':
#     socket_protocol = socket.IPPROTO_IP
# else:
#     socket_protocol = socket.IPPROTO_ICMP
# #开启嗅探
# sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
# sniffer.bind((host,0))
# #设置捕获的数据包中包含的IP头
# sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
# #在Windows平台上，我们需要设置IOCTL以启动混杂模式
# if os.name == 'nt':
#     sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
# #读取单个数据包
# print(sniffer.recvfrom(65565))
# if os.name == 'nt':
#     sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

#3.fast流量
from scapy.all import *
from scapy.layers.dns import DNSRR
dnsRecords={}
def handlePkt(pkt):
    if pkt.haslayer(DNSRR):
        rrname = pkt.getlayer(DNSRR).rrname
        rdata = pkt.getlayer(DNSRR).rdata
        if dnsRecords.has_key(rrname):
            if rdata not in dnsRecords[rrname]:
                dnsRecords[rrname].append(rdata)
        else:
            dnsRecords[rrname] = []
            dnsRecords[rrname].append(rdata)

def main():
    pkts = rdpcap('Demo3.pcap')
    for pkt in pkts:
        handlePkt(pkt)
    for item in dnsRecords:
        print('[+]' + item +'has'+str(len(dnsRecords[item])) +'unique IPs.')
        for i in dnsRecords[item]:
            print("[*]" + i)
if __name__ == '__main__':
    main()