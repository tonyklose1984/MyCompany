#coding:utf-8

#类属性与方法
'''
__private_attrs: 两个下划线开头，声明该属性为私有，不能在类的外部被使用或者直接访问。在类的内部方法中使用时，self.__private_attrs.
'''

class JustCounter:
    __secretCount = 0 #私有变量
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

    def count2(self):
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount
#使用object._className__attrName 访问属性
print counter._JustCounter__secretCount

try:
    counter.count2()
except IOError:
    print "不能调用非共有属性"
else:
    print "ok!"