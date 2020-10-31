# coding=utf-8
import telebot
import requests
import json

bot = telebot.TeleBot("<<TELEGRAM-BOT-TOKEN-CODE>>")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Merhaba {} nasıl yadımcı olabilirim?".format(message.from_user.first_name))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    arg = {'username': '<<CEYD-A-USERNAME>>', 'token': '<<CEYD-A-TOKEN-CODE>>','code': message.text.lower() ,'type':'text','lang':'tr-TR'}
    cevap = json.loads(requests.post("https://beta.ceyd-a.com/jsonengine.jsp", data=arg).content.decode('utf-8')[1:-3]).get("answer")
    bot.send_message(message.chat.id,cevap)


bot.polling()
