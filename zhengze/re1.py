#coding:utf-8

import re

print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
print(re.match(r'^\d{3}\-\d{5}$','010-12345'))

test = '010-12345'
if re.match(r'^\d{3}\-\d{5}$',test):
    print('ok')
else:
    print('failed')
