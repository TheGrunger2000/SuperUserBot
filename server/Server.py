from server.MessageEcho import MessageEcho


class Server:

    def __init__(self):
        self._message = None
        self._message_echo = MessageEcho()

    def set_message(self, message):
        self._message = message

    def get_answer(self):
        return self._message

    def run(self):
        self._message = self._message_echo.run(self._message)
