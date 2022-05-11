import urllib.request
#urllib发起简单请求，获取服务器IP地址
URL_IP = 'https://www.httpbin.org/ip'
def use_simple_urllib():
    response = urllib.request.urlopen(URL_IP)
    print(response.info())
    print("".join(str([line for line in response.readlines()])))
# if __name__ == '__main__':
#     use_simple_urllib()。

# urllib发起get请求
URL_GET = 'https://www.httpbin.org/get'
def use_get_urllib():
    params = urllib.parse.urlencode({'param1':'Hello','param2':'world'})#用urllib.parse.urlencode构造请求参数
    #print("params:" + params)
    #print('?'.join([URL_GET,'%s'])%params)
    URL_GET_Param = '?'.join([URL_GET,'%s'])%params#构造发起GET请求的URL
    response = urllib.request.urlopen(URL_GET_Param)#发起请求
    print("Response Headers:")
    print(response.info())#获取头信息
    print("Response code:")
    print(response.getcode())#获取响应码
    print("Response Body:")
    print(str([line for line in response.readlines()]))#打印响应体
# if __name__ == '__main__':
#     use_get_urllib()

#urllib实现post方法
URL_POST = 'https://www.httpbin.org/post'
def use_post_urllib():
    #1.将post封装到字典
    data = {
        'param1': 'Hello',
        'param2': '苏安院'
    }
    #2.使用parse模块中的urlencode（返回的是字符串类型）进行编码处理
    data = urllib.parse.urlencode(data)
    #3.将步骤2中的结果转换为byte类型
    data = data.encode()
    #4.发起POST请求，data是携带的参数
    response = urllib.request.urlopen(url=URL_POST,data=data)
    data = response.read()
    print(data)
if __name__ == "__main__":
    print("use post params urllib")
    use_post_urllib()