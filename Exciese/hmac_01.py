#coding:utf-8
#Author:TonyHu

from hashlib import sha1
import hmac
import base64

my_sign = hmac.new('123456', '123456', sha1).digest()
my_sign = base64.b64encode(my_sign)
print (my_sign)

# hmac.new(Token,data,hashlib.sha1).digest().encode('base64').rstrip()