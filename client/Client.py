import telebot


class Client:

    def __init__(self):
        self._bot_token = '809780880:AAHX84SLr1b_NAgpD_TqgOC_ERW1PkA19pw'
        self.bot = telebot.TeleBot(self._bot_token)

        self._server = None

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, server):
        self._server = server

    def run(self, token, lang="en", session_id="aibot"):
        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            self.bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

        @self.bot.message_handler(content_types=['text'], commands=['random'])
        def send_text(message):
            self._server.answer = message
            self._server.run(token, lang, session_id)
            answer = self._server.answer
            self.bot.send_message(message.chat.id, answer)

        self.bot.polling()
