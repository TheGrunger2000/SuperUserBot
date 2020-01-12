import telebot
from random_message import random_message


PROXY_ADDRESS = "142.93.72.206"
PROXY_PORT = "3128"

bot = telebot.TeleBot('809780880:AAHX84SLr1b_NAgpD_TqgOC_ERW1PkA19pw')

telebot.apihelper.proxy = {
    'https': 'socks5://{}:{}'.format(PROXY_ADDRESS, PROXY_PORT)
}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = random_message(message.from_user.text, lang='ru')
    bot.send_message(message.from_user.id, answer)


bot.polling(none_stop=True, interval=0)
