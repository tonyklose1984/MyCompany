#coding:utf-8
#Author:TonyHu

from qqbot import _bot as bot

def sendMsgToGroup(msg,groupList,bot):
    for group in groupList:
        bg=bot.List('group', group)
        if bg is not None:
            bot.SendTo(bg[0],msg)

def sendMsgToBuddy(msg,buddyList,bot):
    for buddy in buddyList:
        bd = bot.List('buddy',buddy)
        if bd is not None:
            bot.SendTo(bd[0],msg)

def main(bot):
    groupMsg='今天是个好日子'
    buddyMsg='心想的事儿都能成'
    with open('./qq.txt','r') as fr:
        qqGroup=fr.readline().strip()
        qqBuddy=fr.readline().strip()
    qqGroupList=qqGroup.split(',')
    qqBuddyList=qqBuddy.split(',')
    sendMsgToGroup(groupMsg,qqGroupList,bot)
    sendMsgToBuddy(buddyMsg,qqBuddyList,bot)


if __name__ == '__main__':
    bot.Login(['-q','778228989'])
    main(bot)