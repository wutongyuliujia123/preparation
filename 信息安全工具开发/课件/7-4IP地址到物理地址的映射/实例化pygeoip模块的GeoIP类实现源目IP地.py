#encoding:utf8
import socket
import dpkt
import pygeoip

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getGeoInfo(ip):
    gi = pygeoip.GeoIP('GeoLiteCity.dat')
    rec = gi.record_by_addr(ip)
    return 'ÄÚÍøIP' if rec == None else rec['city']

def getSrcAndDst(packet):
    src_list = []
    dst_list = []
    f = open(packet)
    pcap = dpkt.pcap.Reader(f)
    for item in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(item[1])
            ip = eth.data
            src_list.append(socket.inet_ntoa(ip.src))
            dst_list.append(socket.inet_ntoa(ip.dst))
        except Exception,e:
            print e
    return src_list, dst_list

def main():
    src_list, dst_list = getSrcAndDst('test.pcap')
    for i in range(len(src_list)):
        print('[+] Src: ' + src_list[i] + ' --> Dst: ' + dst_list[i])
        print('[+] Src: ' + getGeoInfo(src_list[i]) + ' --> Dst: ' +getGeoInfo(dst_list[i]))

main()
