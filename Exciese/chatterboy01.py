#coding:utf-8
#Author:TonyHu
from chatterbot import ChatBot
#
# chatbot = ChatBot(
#     'Ron Obvious',
#     trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
# )
#
# chatbot.train('chatterbot.corpus.english')
# chatbot.get_response('Hello, How are you?')

from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi there!",
    "Hello",
])

chatterbot.train([
    "Greetings!",
    "Hello",
])