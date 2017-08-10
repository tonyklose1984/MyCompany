#coding:utf-8
# number = 1
# for day in range(0,9):
#     number = (1+number)*2
# print ('桃子的个数为:',number)
#
# x = input("请输入底数：")
# y = input("请输入幂数：")
# result = 1
# for i in range(0,int(y)):
#     result = result * int(x) %1000
# if result < 100:
#     print('后三位的值为0%d'%(result))
# else:
#     print('后三位的值为%d'%(result))

for man_a in range(1,4):
    for man_b in range(1,4):
        for man_c in range(1,4):
            if((man_a !=1 )&(man_c !=1)&(man_c !=3)&(man_a != man_b)&(man_b!=man_c)&(man_a!=man_c)):
                print('%c将嫁给 A\n'%(chr(ord('X')+man_a-1)))
                print('%c 将嫁给 B\n' % (chr(ord('X') + man_b - 1)))
                print('%c 将嫁给 C\n' % (chr(ord('X') + man_c - 1)))


























