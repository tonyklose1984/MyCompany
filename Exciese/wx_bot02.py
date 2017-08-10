#coding:utf-8
#Author:TonyHu
from wxpy import *

bot = Bot()
#查看对象的puid
# bot.enable_puid('wxpy_puid.pkl')
# my_friend = bot.friends().search("小粒")[0]
#
# #查看她的PUID
# print(my_friend.puid)

# bot.self.add()
# bot.self.accept()
# #发消息给自己
# bot.self.send("能收到吗？")
# #bot.file_helper 文件传输助手
#
# print(bot.friends())
# print(bot.groups())
# print(bot.mps())
# print(bot.chats())

# found = bot.friends().search("小粒")
# xiaoli = ensure_one(found)
# print(xiaoli)
found = bot.friends().search("孙义举")[0]
wxpy_groups = bot.groups().search('IT', [found])
found = wxpy_groups[0].search(province="浙江")
print(found)