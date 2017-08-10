#coding:utf-8
#Author:TonyHu
import requests

r = requests.request("GET","http://www.baidu.com")
print(r.status_code)
r.encoding = 'utf-8'
print(r.text)