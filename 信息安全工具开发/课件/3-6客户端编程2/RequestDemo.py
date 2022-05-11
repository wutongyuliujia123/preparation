import requests
#5.用requests实现简单的客户端访问
URL = 'http://httpbin.org'
#requests简单访问
def use_simple_requests():
    response = requests.get(URL)
    print('>>>>REsponse Headers')
    print(response.headers)
    print('>>>Response Body:')
    print(response.text)
# if __name__ == '__main__':
#     print('>>>Use simple request:')
#     use_simple_requests()

#requests简单GET带参数
import requests
URL_GET = 'http://httpbin.org/get'
def use_params_requests():
        params = {'param1':'hello','param2':'word'}
        print ('Params')
        response = requests.get(URL_GET,params=params)
        print('>>>>REsponse Headers')
        print (response.headers)
        print('>>>Response coder')
        print (response.status_code)
        print('>>>Response Body:')
        print (response.json())
# if __name__ == '__main__':
#     print('>>>Use simple request:')
#     use_params_requests()

#6.用requests库发送请求
import json
import requests
URL = 'https://api.github.com'
def builduri(endpoint):
        return '/'.join([URL,endpoint])
def better_print(json_str):
        return json.dumps(json.loads(json_str),indent = 4)
def request_method():
        response = requests.get(builduri('users/marilynzyw'))
        print (better_print(response.text))

#json模块提供了四个功能：dumps、dump、loads、load，用于字符串 和 python数据类型间进行转换
#dumps是将json对象转换为python对象(  dict转化成str格式  )，dump 把python对象转换为 json对象，把json对象以fp文件流写入文件中
#$loads是将str转化成dict格式，
# if __name__== '__main__':
#         request_method()

#python 中的json模块简介
import json #导入python 中的json模块
l = ['ilovepython',[1,2,3], {'name':'xiaoming'}] #创建一个l列表
encoded_json = json.dumps(l) # 将l列表，进行json格式化编码
# print (repr(l))#repr函数将传入参数转为字符类型
# print (encoded_json) #输出结果

# decode_json = json.loads(encoded_json)
# print (type(decode_json)) #查看一下解码后的对象类型
# print (decode_json) #输出结果

#7.带参数的请求
import requests
def params_request():
        response= requests.get('https://api.github.com/users',params={'since':2})
        print (response.text)
        print (response.request.headers)
        print (response.url)
# if __name__=='__main__':
#         params_request()

def patch_params():
    response = requests.patch('https://api.github.com/user',auth=('zhangyiwei','zyh2cyq2zyw2bd'),json={'name':'marilynzyw1','email':'953453185@qq.com'})
    print (response.url)
    print (response.text)
# if __name__=='__main__':
#     patch_params()


#8.请求的异常处理
from requests import exceptions
def timeout_requests():
    try:
        #将timeout时间改为0.1秒，打印超时信息
        #将timeout时间改为5秒，如果不超时，要求打印出页面的主体信息及响应的状态码。
        response = requests.get('https://api.github.com/users/emails', timeout=5)
    except exceptions.Timeout as e:
        print(e)
    else:
        print(response.text)
        print(response.status_code)
# if __name__ == '__main__':
#     timeout_requests()

#9.响应的基本API
response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.url)
# print(type(response.url))
# print(type(response.headers))
# print(response.history)
# print(response.elapsed)#用response.elapsed查看请求的响应时间
# print(dir(response))#Response提供的API比较多，如果记不清，可以用dir()提供帮助
# print(response.request.headers)#查看request信息，如请求方法和请求的头信息
# print(response)
# print(response.encoding)
# print(response.content)
# print(response.text)#而text得到unicode类型,实际是对内容做了编码。
# print(type(response.json()))
# print(response.json())

#10 下载图片和文本文件
def download_image():
    url = 'https://img.redocn.com/sheji/20211130/aiguojiaoyumingjilishizhanban_11927199.jpg'
    response = requests.get(url)
    print(response.status_code)
    print(response.request.url)
    print(response.request)
    print(response.reason)
    #print(response.content)#接收到的图片内容
    #调用read()方法，会一次性读取全部文件内容，当文件内容较小时比较试用，
    #但是当文件内容过大，很容易导致运行内存100%，所以我们可以反复调用read(size)来设置每次读取的字节内容。
    with open('demo.jpg', 'wb') as image:#
        # write each 128 bytes
        for chunk in response.iter_content(128):#参考链接;https://www.jianshu.com/p/9d2b144bf004
            image.write(chunk)
#download_image()
from contextlib import closing#将打开的流，在块chunk内容读取完后关闭。
def download_image_stream():
    url = 'https://img.redocn.com/sheji/20211130/aiguojiaoyumingjilishizhanban_11927199.jpg'
    #add a context
    with closing(requests.get(url,stream=True)) as response:
        with open('demo11.jpg','wb') as zyh:
            for chunk in response.iter_content(128):
                zyh.write(chunk)
download_image_stream()


