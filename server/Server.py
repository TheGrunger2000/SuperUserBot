from server.MessageEcho import MessageEcho


class Server:

    def __init__(self):
        self._message = None
        self._message_echo = MessageEcho()

    @property
    def answer(self):
        return self._message

    @answer.setter
    def answer(self, message):
        self._message = message

    def run(self, token, lang="en", session_id="aibot"):
        self._message = self._message_echo.run(
            self._message, token, lang, session_id)
