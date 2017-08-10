#coding:utf-8
#Author:TonyHu

from urllib import request

if __name__ == "__main__":
    #访问网址
    url = 'http://www.whatismyip.com.tw/'
    #这是代理ip
    proxy = {'http':'110.250.66.246:8118'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Agent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装opener
    request.install_opener(opener)
    #使用安装好的opener
    response = request.urlopen(url)
    #读取相应的信息并解码
    html = response.read().decode('utf-8')
    #打印信息
    print(html)
