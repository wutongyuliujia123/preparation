#!/usr/bin/env Python
import nmap
import optparse

#nmap 端口扫描
# def nmapScan(tgtHost, tgtPort):
#     nmScan = nmap.PortScanner()
#     nmScan.scan(tgtHost, tgtPort)
#     state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
#     print("[*]" + tgtHost + " tcp/" + tgtPort + "" + state)
#
#
# def main():
#     parser = optparse.OptionParser('using%prog' + '-H <target host> -p <target port>')
#     parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
#     parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
#     (options, args) = parser.parse_args()
#     tgtHost = options.tgtHost
#     tgtPorts = str(options.tgtPort).split(',')
#     if (tgtHost == None) | (tgtPorts[0] == None):
#         print(parser.usage)
#         exit(0)
#     for tgtPort in tgtPorts:
#         nmapScan(tgtHost, tgtPort)
#
#
# if __name__ == '__main__':
#     main()
#python nmapDemo.py -H 192.168.1.17 -p 21,1720,88,22,25,49,69,80,107,115,161,163,443,514

#nmap ping扫描
# import nmap
# import sys
# #本机IP  192.168.1.17
#
# def nmap_ping(host):
#     nm = nmap.PortScanner()
#     result_raw = nm.scan(hosts=host, arguments='-v -n -sn')
#     host_list = []
#     for result in result_raw['scan'].values():
#         if result['status']['state'] == 'up':
#             host_list.append(result['addresses']['ipv4'])
#     return host_list
#
# if __name__ == "__main__":
#     for host in nmap_ping(sys.argv[1]):
#         print('%-20s %5s' % (host, 'is up'))
#python nmapDemo.py  192.168.1.0/24



#ARP 扫描 扫描活动的硬件地址
# -- coding:UTF-8 --
import logging
import sys
# from scapy.all import *
# from scapy.layers.l2 import Ether, ARP
#
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
#
#
# def arp_request(ip_address, queue=None):
#     result = srp(Ether(dst='FF:FF:FF:FF:FF:FF')
#                  / ARP(op=1, hwdst='00:00:00:00:00:00', pdst=ip_address),
#                  timeout=1, verbose=False)
#     try:
#         result_list = result[0].res  # 将响应的数据报对组成为一组清单
#         # [0]为第一组相应的包
#         if queue == None:
#             return result_list[0][1].getlayer(ARP).fields['hwsrc']
#             # [1]接受的包，[0]发送的包
#         else:
#             queue.put((ip_address, result_list[0][1].getlayer(ARP).fields['hwsrc']))
#     except:
#         return
# if __name__ == "__main__":
#     print(arp_request(sys.argv[1]))
    #运行方法 python nmapDemo.py 192.168.1.17
    #定IP


#nmap全能扫描
# -- coding:UTF-8 --
import nmap
import sys
def nmapAscan(host):
    nm = nmap.PortScanner()
    raw_result = nm.scan(hosts=host, arguments='-v -n -A')
    for host, result in raw_result['scan'].items():
        if result['status']['state'] == 'up':
            print('#' * 17 + 'Host:' + host + '#' * 17)
            print('-' * 20 + '操作系统猜测' + '-' * 20)
            for os in result['osmatch']:
                print('操作系统为:' + os['name'] + '准确度为:' + os['accuracy'])
            idno = 1
            try:
                for port in result['tcp']:
                    try:
                        print('-' * 17 + 'TCP服务详细信息' + '[' + str(idno) + ']')
                        idno = idno + 1
                        print('TCP端口号:' + str(port))
                        try:
                            print('状态:' + result['tcp'][port]['state '])
                        except:
                            pass
                        try:
                            print('原因:' + result['tcp'][port]['reason'])
                        except:
                            pass
                        try:
                            print('额外信息:' + result['tcp'][port]['extrainfo'])
                        except:
                            pass
                        try:
                            print('名字:' + result['tcp'][port]['name'])
                        except:
                            pass
                        try:
                            print('版本:' + result['tcp'][port]['version'])
                        except:
                            pass
                        try:
                            print('产品:' + result['tcp'][port]['product'])
                        except:
                            pass
                        try:
                            print('CPE:' + result['tcp'][port]['cpe'])
                        except:
                            pass
                        try:
                            print('脚本:' + result['tcp'][port]['script'])
                        except:
                            pass
                    except:
                        pass
            except:
                pass

if __name__ == "__main__":
    print(nmapAscan(sys.argv[1]))