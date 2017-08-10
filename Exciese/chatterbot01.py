#coding:utf-8
#Author:TonyHu

# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot import *
#
# chatterbot = ChatBot("Training Example")
# chatterbot.set_trainer(ListTrainer)
#
# chatterbot.train(
#     [
#         "Hi there",
#         "Hello",
#     ]
# )
#
# chatterbot.train([
#     "Greetings!",
#     "Hello",
# ])
#
# chatterbot.train([
#     "How are you?",
#     "I am good",
#     "That os good to her",
#     "Thank you",
#     "You Are welcome",
# ])
#
# chatterbot = ChatBot("Training Example")
# chatterbot.set_trainer(ChatterBotCorpusTrainer)
# chatterbot.train([
#     "chatterbot.corpus.english",
#     "chatterbot.corpus.english.greetings",
#     "chatterbot.corpus.english.conversations"
# ])
#
from chatterbot import ChatBot
bot = ChatBot('Norman')

# from chatterbot.trainers import ListTrainer
#
# chatbot = ChatBot("Tony Huang")
# conversation = [
#     "Hello",
#     "Hi There!",
#     "How are you doing?",
#     "i'm doing great",
#     "that is good to her",
#     "thank you",
#     "you're welcome",
#     "what the fuck",
#     "i will do my best",
#     "i am five yeats old",
# ]
#
# chatbot.set_trainer(ListTrainer)
# chatbot.train(conversation)
#
# response = chatbot.get_response("how old are you?")
# print(response)















