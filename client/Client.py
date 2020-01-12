import telebot
from server.Server import Server


class Client:

    def __init__(self):
        self._bot_token = '809780880:AAHX84SLr1b_NAgpD_TqgOC_ERW1PkA19pw'
        self.bot = telebot.TeleBot(self._bot_token)

        self._server = Server()

        self.proxy_address = None
        self.proxy_port = None

    def set_proxy_address(self, proxy_address):
        self.proxy_address = proxy_address

    def set_proxy_port(self, proxy_port):
        self.proxy_port = proxy_port

    def run(self, token, lang="en", session_id="aibot"):
        telebot.apihelper.proxy = {
            'https': 'socks5://userproxy:password@{}:{}'.format(self.proxy_address, self.proxy_port)
        }

        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            self.bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

        @self.bot.message_handler(content_types=['text'], commands=['random'])
        def send_text(message):
            self._server.answer = message
            self._server.run(token, lang, session_id)
            answer = self._server.answer
            self.bot.send_message(message.chat.id, answer)

        self.bot.polling(none_stop=True, interval=0)
