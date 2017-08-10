#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import hashlib
import requests
import hmac
import base64
from urllib import parse, request
import time
import json

def make_digest(message, key):
    message = bytes(message, 'UTF-8')
    key = bytes(key, 'UTF-8')
    digester = hmac.new(key, message, hashlib.sha1)
    signature1 = digester.digest()
    signature2 = base64.urlsafe_b64encode(signature1)
    return str(signature2, 'UTF-8')

# result = make_digest('aaaaaaa', 'dkdkdkdkdk')

now_time = time.strftime('%Y%m%d%H%M%S')
# print(now_time)
a = parse.quote_plus('/car/v1_5/status/detail')
#print(a)

b = parse.quote_plus('deviceNum=116502100007366&lpNum=京QV76D1&reqTime=' + now_time + '&uid=BQXNY00001')
#print(b)

c = a + b
print(c)
sign = make_digest(c, 'Bqxny20161115')

#print(sign)


load1 = {"uid": 'BQXNY00001',
                 "reqTime": now_time,
                 "lpNum": "京QV76D1",
                 "deviceNum": "116502100007366",
                 "sign": sign,
                 }

json_data = json.dumps(load1).encode('GB2312')
print(json_data)


headers = {'content-type': 'application/json',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


# req = requests.request('GET','http://api.feezu.cn/car/v1_5/status/detail', data=json_data,headers=headers)
# print(req.status_code)
# print(req.text)

try:
    r = requests.get('http://api.feezu.cn/car/v1_5/status/detail',data=json_data)
    r.raise_for_status()
    print(r.status_code)
    print(r.apparent_encoding)
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("产生了异常")



# response = request.urlopen(req)
# data = response.read()
# print(data.decode('UTF-8'))























