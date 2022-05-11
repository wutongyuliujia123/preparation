import re
import requests
def getHTMLText (url) :
    try :
       r = requests.get(url, timeout = 30)
       #print(r.text)
       return r.text
    except:
        return ""

def parsePage(infolist, html):
    print("进入")
    try:
        plt = re.findall(r'&yen;[\d]*\.[\d]*', html)#正则表达式匹配价格
        tlt = re.findall(r'title=".*"  ddclick=',html)#正则表达式匹配书名
        #print("plt"+plt.__str__())
        #print("tlt"+tlt.__str__())
        #print(len(tlt))
        for i in range(len(tlt)):
            price = plt[i].split(';')[1]#用;切分
            #print(price)
            title = tlt[i].split('"')[1]#用”切分
            infolist.append([price, title])#以元组的形式放到infolist中
    except:
        print("出错")
def printGoodsList(infolist):
    tplt = "{:4}\t{:8}\t{:16}"#构造\t进行缩进
    print(tplt.format("序号","价格","商品名称"))#format是格式化函数，参考：https://www.runoob.com/python/att-string-format.html
    count = 0
    for g in infolist:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))#编号，价格，书名
def main():
    goods = 'java'
    depth = 3
    index = '&act=input&page_index='
    start_url = 'http://search.dangdang.com/?key='
    infoList = []
    for i in range(depth):
        try:
            url = start_url + goods + index + str(i+1)
            print(url)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
main()