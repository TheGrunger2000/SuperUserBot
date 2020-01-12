# -*- coding: utf-8 -*-
import telebot
from random_message import random_message

bot = telebot.TeleBot('809780880:AAHX84SLr1b_NAgpD_TqgOC_ERW1PkA19pw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = random_message(message.from_user.text, lang='ru')
    bot.send_message(message.from_user.id, answer)


bot.polling(none_stop=True, interval=0)
