#coding:utf-8
#Author:TonyHu
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != k) and (i != j) and (j != k):
#                 print i,j,k

#使用列表形式，进行计算总结
# d = []
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if (a!=b) and (b!=c) and (a!=c):
#                 d.append([a,b,c])
# print "总数量:",len(d)
# print d

#将for循环和if语句综合成为一句，直接打印出结果
# list_num = [1,2,3,4]
#
# list = [i*100+j*10+k for i in list_num for j in list_num for k in list_num if (j!=i and k!=j and k!=i) ]
# print len(list)
# print list

#设置最大值，最小值
# line = []
# for i in range(123,433):
#     a = i % 10
#     b = (i%100)//10
#     c = (i%1000)//100
#     if a!=b and b!=c and a!=c and 0<a<5 and 0<b<5 and 0<c<5:
#         print i
#         line.append(i)
# print ("the total is:",len(line))

#利用集合去除重复元素
# import pprint
# list_num = ['1','2','3','4']
# list_result = []
# for i in list_num:
#     for j in list_num:
#         for k in list_num:
#             if len(set(i+j+k))==3:
#                 list_result += [int(i+j+k)]
#
# print("能组成%d个互不相同且无重复的三位数："%len(list_result))
# pprint.pprint(list_result)

#利用内置函数
# from itertools import permutations
# data = []
# for i in permutations([1,2,3,4],3):
#     data.append(i)
#     print data
#
# print ("一共有%d种组合方法"%len(data))

for num in range(6,58):
    a = num >> 4 & 3
    b = num >> 2 & 3
    c = num & 3
    if((a^b) and (b^c) and (c^a)):
        print a+1,b+1,c+1






















