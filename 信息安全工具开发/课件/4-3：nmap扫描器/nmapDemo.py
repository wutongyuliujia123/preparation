import logging
import sys
import nmap
import optparse
#安装命令：pip install python-nmap
#1.nmap端口扫描
# def nmapScan(tgtHost,tgtPort):
#     nmScan = nmap.PortScanner()#创建nmap端口扫描
#     nmScan.scan(tgtHost,tgtPort)##设置主机名tgtHost和端口号tgtPort
#     state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']#扫描结果记录
#     print("[*]" + tgtHost + "tcp/" +tgtPort + "  " + state)#打印扫面结果
# def main():
#     parser = optparse.OptionParser('using%prog' + '-H <target host> -P <target port>')
#     parser.add_option('-H',dest = 'tgtHost' ,type='string' ,help = 'host')
#     parser.add_option('-P',dest = 'tgtPort' ,type='string' ,help = 'Port')
#     (options,args) = parser.parse_args()#构建元组
#     tgtHost = options.tgtHost#拿到主机IP
#     tgtPorts = str(options.tgtPort).split(',')#对端口号进行切分，用‘，’切分
#     if(tgtHost == None) | (tgtPorts[0] == None):#判断端口号和主机名是否为空
#         print(parser.usage)
#         exit(0)
#     for tgtPort in tgtPorts:
#         nmapScan(tgtHost,tgtPort)#循环发起扫描
# if __name__ == "__main__":
#     main()
    #在命令行模式下，进入本文件所在的目录，执行下面语句，
    #python nmapDemo.py -H 192.168.1.17 -P 3306,21,80,25,115
# #Ip换成自己的IP，nmapDemo.py换成自己的文件名

#2.nmap ping扫描
# def nmap_ping(host):
#     nm = nmap.PortScanner()#创建端口扫描
#     result_raw = nm.scan(hosts=host,arguments='-v -n -sn')
#     host_list = []#保存存活主机的数组
#     for result in result_raw['scan'].values():#发起ping扫描
#         if result['status']['state'] == 'up':#判断主机是否存活
#             host_list.append(result['addresses']['ipv4'])#将结果保存到host_list
#     return host_list
# if __name__ == '__main__':
#     for host in nmap_ping(sys.argv[1]):#接收参数
#         print("%-20s %5s" % (host,'is up'))#打印存活主机
    # 在命令行模式下，进入本文件所在的目录，执行下面语句
    #python nmapDemo.py 192.168.1.0/24
# #Ip换成自己的IP，nmapDemo.py换成自己的文件名

#3.ARP 扫描 扫描活动的硬件地址
from scapy.layers.l2 import Ether, ARP
from scapy.all import *
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
def arp_request(ip_address,queue = None):
    #构建扫描结果
    result = srp(Ether(dst='FF:FF:FF:FF:FF:FF') / ARP(op=1,hwdst='00:00:00:00:00:00',pdst = ip_address),timeout=1,verbose=False)
    try:
        result_list = result[0].res#将结果数组的第一个元素放入结果列表
        if queue == None:#判断队列是否为空
            return result_list[0][1].getlayer(ARP).fields['hwsrc']
        else:
            queue.put((ip_address,result_list[0][1].getlayer(ARP).fields['hwsrc']))
    except:
        return
if __name__ == '__main__':
    print(arp_request(sys.argv[1]))#调用arp扫描
    # 在命令行模式下，进入本文件所在的目录，执行下面语句
    #python nmapDemo.py 192.168.1.17
    # #Ip换成自己的IP，nmapDemo.py换成自己的文件名