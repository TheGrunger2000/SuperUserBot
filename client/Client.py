class Client:

    def __init__(self):
        self._message = None
        self._server = None

    def print_message(self):
        print(self._message)

    @property
    def message(self):
        return self._message

    @property
    def server(self):
        return self._server

    @message.setter
    def message(self, message):
        self._message = message

    @server.setter
    def server(self, server):
        self._server = server

    def run(self, token, lang="en", session_id="aibot"):
        self._server.message = self._message
        self._server.run(token, lang, session_id)
        self._message = self._server.answer
