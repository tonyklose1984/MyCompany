#coding:utf-8


# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print "Name : " ,self.name,", Salary:" ,self.salary
#
# emp1 = Employee("Zara",2000)
# emp2 = Employee("Manni",5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount
# emp1.age = 7
# emp1.age = 8
# #del emp1.age
# print hasattr(emp1,'age')
# print getattr(emp1,'age')
# setattr(emp1,'age',90)
# print getattr(emp1,'age')
# delattr(emp1,'age')

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
#
# t.prt()

# class Employee:
#     empCount = 0
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" %Employee.empCount
#
#     def displayEmployee(self):
#         print "Name: ",self.name,", Salary:",self.salary
#
# print "Employee.__doc__",Employee.__doc__
# print "Employee.__name__:", Employee.__name__
# print "Employee.__module__:", Employee.__module__
# print "Employee.__bases__:", Employee.__bases__
# print "Employee.__dict__:", Employee.__dict__

# a = 40
# b = a
# c = [b]
#
# del a
# b = 100
# c[0] = -1
# print (b,c)

# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print class_name,"销毁"
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print id(pt1),id(pt2),id(pt3)
# del pt1
# del pt2
# del pt3

# class Parent:
#     parentAttr = 100
#     def __init__(self):
#         print '调用父类构造函数'
#
#     def parentMethod(self):
#         print "调用父类方法"
#
#     def setAttr(self,attr):
#         Parent.parentAttr = attr
#
#     def getAttr(selfs):
#         print "父类属性：",Parent.parentAttr
#
#
# class Child(Parent):  # 定义子类
#     def __init__(self):
#         print "调用子类构造方法"
#
#     def childMethod(self):
#         print '调用子类方法 child method'
#
#
# c = Child()  # 实例化子类
# c.childMethod()  # 调用子类的方法
# c.parentMethod()  # 调用父类方法
# c.setAttr(200)  # 再次调用父类的方法
# c.getAttr()  # 再次调用父类的方法
#
# print(isinstance(c,Parent))
#
# #方法重写
# class Parent:
#     def myMethod(self):
#         print "调用父类方法"
#
# class Child(Parent):
#     def myMethod(self):
#         print "调用重新定义子类方法"
#
# c = Child()
# c.myMethod()

# __init__(self,[,args...]) , __del__(self) , __repr__(self) , __str__(self) , __cmp__(self,x)

#运算符重载(__add__,__sub__,__mul__,__div__)
# class Vector:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d,%d)'%(self.a,self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#     def __sub__(self, other):
#         return Vector(self.a - other.a, self.b - other.b)
#
#     def __mul__(self, other):
#         return Vector(self.a * other.a, self.b * other.b)
#
#     def __div__(self, other):
#         return Vector(self.a / other.a, self.b / other.b)
#
# v1 = Vector(8,10)
# v2 = Vector(2,-2)
#
# print v1 + v2
# print v1 - v2
# print v1 * v2
# print v1 / v2



