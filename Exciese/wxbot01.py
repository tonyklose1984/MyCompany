#coding:utf-8
#Author:TonyHu
from wxpy import *

bot = Bot()
my_friend = bot.search("韩羽")[0]
tuling = Tuling(api_key='2911bc96055641338af2eaf21a611d87')

@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
bot.join()

# bot.join()
# bot.self.add()
# bot.self.accept()
# bot.self.send("能收到吗？")
# bot.friends('小粒')

# my_friend.send("Hello,我是小机器人。")
#向文件助手发送消息
# bot.file_helper.send("hello from wxpy")


# #自动回复所有文字消息
# @bot.register(msg_types=TEXT)
# def auto_reply_all(msg):
#     tuling.do_reply(msg)
