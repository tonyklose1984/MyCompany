#coding:utf-8

import re
img_pat = '"pic_url":"(//.*?)"'
ziduan = '"pic_url":"//g-search3.alicdn.com/img/bao/uploaded/i4/i2/TB1yY8GLpXXXXX6XXXXXXXXXXXX_!!0-item_pic.jpg","detail_url":"//detail.tmall.com/item.htm?id\u003d536564643951\u0026ad_id\u003d\u0026am_id\u003d\u0026cm_id\u003d140105335569ed55e27b\u0026pm_id\u003d\u0026abbucket\u003d1","view_price":"59.00","view_fee":"0.00"'
imgL = re.compile(img_pat).findall(ziduan)
print(imgL)