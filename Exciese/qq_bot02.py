#coding:utf-8
#Author:TonyHu
# from qqbot import _bot as bot
import qqbot

# bot.Login(['-q',"154293106"])
#
# user_list = bot.List('buddy')
# for user in user_list:
#     print(user)
#
# group_list = bot.List('group')
# for group in group_list:
#     print(group)
# user = bot.List("buddy","域学习朋友")[0]
# bot.SendTo(user,"机器人收到请回复~")

#写自动回复
@qqbot.QQBotSlot
def onQQMessage(bot,contact,member,content):
    '''

    :param bot:  #QQ对象
    :param contact:   #QQ发信人
    :param member:    #发消息的对象，只对群组有作用
    :param content:   #内容
    :return:
    '''
    if content == "-hello":
        bot.SendTo(contact,"你也好啊，/龇牙")
    elif "@ME" in content:
        bot.SendTo(contact,"/菜刀 咋的了？")

if __name__ == "__main__":
    qqbot.RunBot()

# bot.Stop()
